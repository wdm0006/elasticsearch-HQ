ElasticHQ - Version 3.0 - In Development
========================================

This version is considered experimental until a formal v3.0GA release. Until then, please see instructions on the [master branch](https://github.com/ElasticHQ/elasticsearch-HQ/tree/master) of this repository.

For the formal announcement of this version, [see here](https://groups.google.com/forum/#!topic/elastichq/rZOBFNePRKg).

Notes + Support
---------------

* Google Group can be found here: https://groups.google.com/d/forum/elastichq
* If you need sample index + documents, see here: https://github.com/royrusso/elasticsearch-sample-index
* If you find a bug, **please** create an issue and report it, or fix it and let me know. ;-)
 
Running the Docker Container
----------------------------

    docker build -t eshq .
    docker run -p 5000:5000 -t eshq

Database Migrations
-------------------
    
    export ELASTICHQ_ENV=DEV|TEST|PROD
    python manage.py db init # if first time running migration
    python manage.py db migrate
    python manage.py db upgrade

Interactive Shell
-----------------
    
    export ELASTICHQ_ENV=DEV|TEST|PROD
    python manage.py shell

License
-------

See included [License File](LICENSE.md).


