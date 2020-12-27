import importlib
import pkgutil

def list_versions():
    result = []
    for _, name, _ in pkgutil.iter_modules(['nrv']):
        if name.startswith('v') and name[1:].isalnum():
            result.append(name)
    return result


def get_version(version, exclude_uppercase=True):
    v =  importlib.import_module('nrv.%s' % version)
    result = []
    for role in v.data:
        result.append('::%s' % role)
        for kind in v.data[role]:
            if not kind.isupper():
                result.append('::%s:%s' % (role, kind))
    return result

