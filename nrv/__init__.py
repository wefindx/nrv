import importlib
import pkgutil
import os

def list_versions():
    result = []
    pkg = importlib.import_module('nrv')
    pkgpath = os.path.dirname(pkg.__file__)
    for _, name, _ in pkgutil.iter_modules([pkgpath]):
        if name.startswith('v') and name[1:].isalnum():
            result.append(name)
    return result


def get_version(version=None, exclude_uppercase=True):
    if version is None:
        latest = max([int(v[1:]) for v in list_versions()])
        version = 'v%s' % latest

    v =  importlib.import_module('nrv.%s' % version)
    result = []
    for role in v.data:
        result.append('::%s' % role)
        for kind in v.data[role]:
            if not kind.isupper():
                result.append('::%s:%s' % (role, kind))
    return result


def validate_name(name):
    'Validate Collection Name'

    version = None

    if '::v' in name:
        tok = name.split('::v', 1)[-1]
        num = tok.split('/', 1)[0]
        if '/' in tok and num.isalnum():
            version = 'v%s' % num
            name = '::'.join(name.split('::%s/' % version))

            if version not in list_versions():
                return False

    return any([token in name for token in get_version(version)])
