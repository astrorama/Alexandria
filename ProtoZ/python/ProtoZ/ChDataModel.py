import os.path
import os
import glob
from astropy.table import Table

def _read_xy_dataset_file(file):
    if not os.path.isfile(file):
        return None
    name = file[file.rfind('/')+1:]
    if '.' in name:
        name = name[:name.rfind('.')]
    with open(file) as f:
        firstLine = f.readline().strip()
        if firstLine.startswith('#') :
            name = firstLine[1:].strip()
            if ' ' in name:
                name = name[:name.find(' ')]
    data = Table.read(file, format='ascii')
    return (name, data)

def _read_xy_datasets_from_dir(path):
    if not os.path.isdir(path):
        return None
    datasets = {}
    for file in glob.glob(path+'/*'):
        name, data = _read_xy_dataset_file(file)
        datasets[name] = data
    return datasets

def get_filters(path):
    return _read_xy_datasets_from_dir(path)

def get_seds(path):
    return _read_xy_datasets_from_dir(path)

def get_reddening_curves(path):
    return _read_xy_datasets_from_dir(path)