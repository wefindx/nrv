Network Resource Vocabulary
===========================

This is a repository to version NRV -- network resource vocabulary.

``pip install nrv``

Usage
-----

::

    import nrv

    nrv.list_versions()

    nrv.get_version('v1')

    nrv.validate('example.com/Person::v1/system:person')


Development
-----------

::

    pip install pytest

    py.test


Create a PR to suggested new version, name it as new file, with ``v$``,
where ``$`` is a natural number.
