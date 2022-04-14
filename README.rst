Dengue Dashboard
=================



.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT
Already got started?
--------------------
When you already got started you just need to run 

    $ sudo docker-compose -f local.yml up

And in another shell: 

    $ sudo npm run serve

And open http://localhost:8000/.

Or when you're running a linux distribution just execute 

    $ sudo sh beammeup.sh

in dengue-dashboard folder.




This project is part of the Bachelorreport of Jennifer Horstmann submitted to the faculty of Mathematics and Computer Science at the University of Bremen for the degree of Bachelor of Science.


Getting started
---------------

Back end: Django
================

Getting Up and Running Locally With Docker
------------------------------------------


The steps below will get you up and running with a local development environment.
All of these commands assume you are in the root of your generated project.

See also: https://github.com/pydanny/cookiecutter-django/

Prerequisites
-------------

* Docker; if you don't have it yet, follow the `installation instructions`_;
* Docker Compose; refer to the official documentation for the `installation guide`_.

.. _`installation instructions`: https://docs.docker.com/install/#supported-platforms
.. _`installation guide`: https://docs.docker.com/compose/install/


Build the Stack
---------------

This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f local.yml build

Generally, if you want to emulate production environment use ``production.yml`` instead. And this is true for any other actions you might need to perform: whenever a switch is required, just do it!


Run the Stack
-------------

This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f local.yml up

You can also set the environment variable ``COMPOSE_FILE`` pointing to ``local.yml`` like this::

    $ export COMPOSE_FILE=local.yml

And then run::

    $ docker-compose up

To run in a detached (background) mode, just::

    $ docker-compose up -d


Execute Management Commands
---------------------------

As with any shell command that we wish to run in our container, this is done using the ``docker-compose -f local.yml run --rm`` command: ::

    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Here, ``django`` is the target service we are executing the commands against.


More on Docker and local development can be found in "LOCAL_DEV.rst".


Front end: Vue.js
=================

This app integrates with a Vue single page app (SPA) located in ``vue_frontend``.

To initialize the frontend, from the ``vue_frontend`` directory, run::

    $ npm install

To serve the Vue frontend in hot-reloading development mode::

    $ npm run serve

And to build for deployment::


    $ npm run build

For more information, see ``vue_frontend/README.md``.





Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.



Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html






Future Works
------------

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy dengue_dashboard

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest
