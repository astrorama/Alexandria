import os
import sys
import pyxb.utils.domutils as domutils
import CommonDM.dm.nonamespace_stub as stub
import CommonDM.dm.pro.phz_stub as phz_stub
import CommonDM.dmtools as dmtools

def getApplicationName():
    return 'PhotometryToLikelihood'

def generateCommandParameters(input_files_dict, output_files_dict):
    parameters = []
    parameters.extend(_generatePhotometryCatalogParam(input_files_dict))
    parameters.extend(_generateModelPhotometryMatrixParam(input_files_dict))
    parameters.extend(_generatePhzCatalogParam(output_files_dict))
    return parameters

def postProcessOutput(output_files_dict, exec_command):
    _createPhzCatalogXml(output_files_dict, exec_command)

def _generatePhotometryCatalogParam(input_files_dict):
    parameters = []
    phot_cat_xml = input_files_dict.get('PhotometricCatalog')
    if not phot_cat_xml:
        phot_cat_xml = input_files_dict.get('')
    if not phot_cat_xml or not os.path.isfile(phot_cat_xml):
        raise Exception('PhotometricCatalog input XML file parameter is missing')
    dom = domutils.StringToDOM(file(phot_cat_xml).read())
    phot_cat = stub.PHZPhotometryCatalog.createFromDOM(dom)
    phot_cat_fits = dmtools.getFileFromDataContainer(phot_cat.Data.DataContainer)
    # If the FITS path is relative we prefix it with the path of the XML file
    if not phot_cat_fits.startswith(os.sep):
        phot_cat_fits = os.path.abspath(os.path.dirname(phot_cat_xml)) + os.sep + phot_cat_fits
    parameters.append('--photometric-catalog=' + phot_cat_fits)
    parameters.append('--photometric-catalog-format=FITS')
    return parameters

def _generateModelPhotometryMatrixParam(input_files_dict):
    parameters = []
    print input_files_dict
    calib_data_xml = input_files_dict.get('CalibrationData')
    if calib_data_xml:
        dom = domutils.StringToDOM(file(calib_data_xml).read())
        calib_data = stub.PHZCalibrationData.createFromDOM(dom)
        model_phot_matrix = dmtools.getFileFromDataContainer(calib_data.Data.CalibrationModel[0].Model)
        if not model_phot_matrix.startswith(os.sep):
            model_phot_matrix = os.path.abspath(os.path.dirname(calib_data_xml)) + os.sep + model_phot_matrix
        parameters.append('--model-photometry-matrix=' + model_phot_matrix)
    return parameters

def _generatePhzCatalogParam(output_files_dict):
    parameters = []
    phz_cat_xml = output_files_dict.get('PhzCatalog')
    if not phz_cat_xml:
        phz_cat_xml = output_files_dict.get('')
    if not phz_cat_xml:
        raise Exception('PhzCatalog output XML file parameter is missing')
    phz_cat = os.path.abspath(os.path.dirname(phz_cat_xml)) + os.sep
    phz_cat += dmtools.createEuclidFilename('PHZCAT', 'fits')
    parameters.append('--phz-catalog=' + phz_cat)
    return parameters

def _createPhzCatalogXml(output_files_dict, exec_command):
    phz_cat_xml = output_files_dict.get('PhzCatalog')
    if not phz_cat_xml:
        phz_cat_xml = output_files_dict.get('')
    for param in exec_command:
        if param.startswith('--phz-catalog='):
            phz_cat_fits = param.replace('--phz-catalog=', '')
    print >> sys.stderr, 'Creating ' + phz_cat_xml + ' file'
    root = stub.PHZPhotoZCatalog()
    root.Header = dmtools.createGenericHeader()
    root.Data = phz_stub.photoZCatalog.Factory()
    root.Data.DataContainer = dmtools.createDataContainerForFile(phz_cat_fits, 'FITS', 'PHZ catalog')
    out_file = open(phz_cat_xml, 'w')
    out_file.write(root.toDOM().toprettyxml())
    out_file.close()
    