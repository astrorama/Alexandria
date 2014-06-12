import os
import datetime
import time
import hashlib
import CommonDM.dm.sys.sgs_stub as sgs_stub
import CommonDM.dm.sys_stub as sys_stub

class LocalFileUnavailable(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def getFileFromDataContainer(dc):
    """Extracts the local filename from a data container.

    Args:
        dc: The DataContainer PyXB stub

    Returns:
        A string containing the name of the local file

    Raises:
        LocalFileUnavailable: If the data container does not contain a local
            storage node.
    """
    for loc in dc.Location:
        if loc.StorageNode.Sdc == 'LOCAL' and loc.StorageNode.Protocol == 'file':
            filename = dc.Filename
            if loc.Path:
                filename = loc.Path + os.sep + filename
            if loc.StorageNode.BasePath:
                filename = loc.StorageNode.BasePath + os.sep + filename
            if not filename.startswith(os.sep) and hasattr(dc, '_euclidOriginalFilename'):
                 filename = os.path.abspath(os.path.dirname(dc._euclidOriginalFilename)) + os.sep + filename
            return filename
    raise LocalFileUnavailable('Error: No local file for DataContainer ' + str(dc.Id))

def createDataContainerForFile(filename, type, description):
    """Creates a data container PyXB stub which represents the given file.
    
    Note that only files in the same directory with the output XML file are
    allowed. It is the responsibility of the user to copy the file in this
    directory. The file name is assumed to follow the Euclid format, so the last
    23 characters before the last '.' (before the postfix) should give the
    creation date of the file.
    
    Args:
        - filename: The name of the file (path will be stipped out)
                  (ex: EUC-TEST-NONEXIST-2013-08-05T152700.000.fits)
        - type: The type of datacontainer (ex: FITS image)
        - description: A short description of the content
         
    Returns:
        A data container PyXB stub representing the file
    
    Raises:
        IOError: If the given file does not exist
    """
    name = os.path.basename(filename)
    dc = sgs_stub.dataContainer()
    dc.Id = str(int(time.time() * 1E6))
    dc.Filename = name
    dc.Description = description
    dc.Type = type
    creationDate = '-'.join(filename.split('-')[3:])
    creationDate = '.'.join(creationDate.split('.')[:2])
    if creationDate.endswith('Z'):
        creationDate = creationDate[:-1]
    if creationDate.find(':') == -1:
        creationDate = creationDate[:13]+':'+creationDate[13:15]+':'+creationDate[15:]
    dc.CreationDate = creationDate
    dc.CheckSum = _createCheckSum(filename)
    return dc

def _createCheckSum(filename):
    """Returns a PyXB checksumType stub for the given file."""
    checkSum = sgs_stub.checksumType()
    checkSum.Algorithm = 'MD5'
    checkSum.Value = _md5ForFile(filename)
    return checkSum

def _md5ForFile(filename, block_size=2**20):
    """Generates the MD5 checksum for the given file"""
    f = open(filename, 'rb')
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    f.close()
    return md5.hexdigest()

def createEuclidFilename(file_type, extension):
    date_string = datetime.datetime.isoformat(datetime.datetime.utcfromtimestamp(time.time()))
    date_string = date_string[:-3]
    return 'EUC-TEST-' + file_type + '-' + date_string + '.' + extension

def createGenericHeader():
    header = sys_stub.genericHeader()
    header.ProductId = 0
    header.ProductName = 'PhotoZCatalog'
    header.ProductType = 'FITS'
    header.SoftwareName = 'SDC-CH Prototype'
    header.SoftwareRelease = '0.1'
    header.ScientificCustodian = 'PHZ'
    acr = sys_stub.accessRights()
    acr.EuclidConsortiumRead = True
    acr.EuclidConsortiumWrite = False
    acr.ScientificGroupRead = True
    acr.ScientificGroupWrite = True
    header.AccessRights = acr
    return header