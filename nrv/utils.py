import importlib
import pkgutil
import os

from boltons.iterutils import remap
from collections import defaultdict


def get_valid_codes(data):
    result = defaultdict(list)

    def visit(path, key, value):
        if isinstance(key, int):
            if key % 100:
                result[100* (key // 100)].append(key)
        return key, value

    remap(data, visit=visit)
    return dict(result)


def get_valid_names(data, lang='en'):
    result = defaultdict(dict)

    def visit(path, key, value):
        if isinstance(key, int):
            if key % 100:
                key_in_words = 100 * (key // 100)
                vals_in_langs = data[key_in_words]
                vals_in_words = [item.get(lang) for item in vals_in_langs.values()]
                result[vals_in_words[0]] = vals_in_words[1:]
        return key, value

    remap(data, visit=visit)
    return dict(result)

def list_versions():
    result = []
    pkg = importlib.import_module('nrv')
    pkgpath = os.path.dirname(pkg.__file__)
    for _, name, _ in pkgutil.iter_modules([pkgpath]):
        if name.startswith('v') and name[1:].isalnum():
            result.append(name)
    return result

def get_latest_version():
    latest = max([int(v[1:]) for v in list_versions()])
    version = 'v%s' % latest
    return version


## MAIN FUNCTIONS ##


def get_version(version=None, exclude_uppercase=True, include_top=True):
    ''' names '''

    if version is None:
        version = get_latest_version()

    v =  importlib.import_module('nrv.%s' % version)
    result = []

    if version == 'v1':
        v_names = v.data
    else:
        v_names = get_valid_names(v.data)

    for key in v_names:
        if include_top:
            result.append('::%s' % key)
        for val in v_names[key]:
            if not val.isupper():
                result.append('::%s:%s' % (key, val))
    return result


def get_version_codes(version=None, include_top=True):
    '''' codes '''

    if version is None:
        version = get_latest_version()

    v =  importlib.import_module('nrv.%s' % version)

    if version == 'v1':
        v_codes = []
    else:
        v_codes = get_valid_codes(v.data)


    result = []
    for key in v_codes:
        if include_top:
            result.append('::%s:' % key)
        for val in v_codes[key]:
            result.append('::%s' % val)

    return result
