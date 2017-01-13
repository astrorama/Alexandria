import os

def find_conf_file(package, executable):
    name = os.sep + package + os.sep + executable + '.conf';
    for confPath in os.environ.get('ELEMENTS_CONF_PATH').split(':'):
        if os.path.isfile(confPath + name):
            confFile = confPath + name
            break
    return confFile

def parse_conf_file(file):
    conf = {}
    with open(file) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('#') or not '=' in line:
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            if '#' in value:
                value = value[:value.find('#')]
            if (not conf.has_key(key)):
                conf[key] = []
            conf[key].append(value)
    return conf