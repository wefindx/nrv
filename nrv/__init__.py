from .utils import (
    list_versions,
    get_latest_version,
    get_valid_codes,
    get_valid_names,

    get_version,        # Returns valid names for version.
    get_version_codes,  # Returns valid codes for version.
)


def validate(codename, include_top=False):
    'validate table name'

    version = None

    if '::v' in codename:
        tok = codename.split('::v', 1)[-1]
        num = tok.split('/', 1)[0]
        if '/' in tok and num.isalnum():
            version = 'v%s' % num
            codename = '::'.join(codename.split('::%s/' % version))

            if version not in list_versions():
                return False

            # include_top -- False, cause there would be very many False positives, for now.
            valid_names = get_version(version, include_top=include_top)
            valid_codes = get_version_codes(version, include_top=include_top)

            valid_codenames = valid_codes + valid_names

    return any([token in codename for token in valid_codenames])


