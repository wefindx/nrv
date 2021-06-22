Network Resource Vocabulary
===========================

This is a repository to version NRV -- network resource vocabulary. Review `v3 codes <./nrv/v3.py>`_.

``pip install nrv``

Usage
-----

::

    import nrv

    nrv.list_versions()

    nrv.get_version('v3')

    nrv.validate('example.com/Person::v1/system:person')
    
    # or #
    
    nrv.validate('example.com/Person::v3/470')


Development
-----------

::

    pip install pytest

    py.test


Create a PR to suggested new version, name it as new file, with ``v$``,
where ``$`` is a natural number.
