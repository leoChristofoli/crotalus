crotalus
========

Personal protfolio page

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html


- Antaresia
    - Antaresia childreni, Children's python
    - Antaresia maculosa, Spotted python
    - Antaresia perthensis, Pygmy python
    - Antaresia stimsoni, Stimson's python
- Apodora, Papuan python
    - Apodora papuana, Papuan python
- Aspidites
    - Aspidites melanocephalus, Black-headed python
    - Aspidites ramsayi, Woma
-Bothrochilus, Bismark ringed python
    - Bothrochilus boa, Bismark ringed python
- Leiopython, D'Albert's water python
    - Leiopython albertisii, D'Albert's water python
    - Leiopython bennettorum, Bennett's white-lipped python
    - Leiopython biakensis, Biak white-lipped python
    - Leiopython fredparkeri, Parker's white-lipped python
    - Leiopython hoserae, southern white-lipped python
    - Leiopython huonensis, Huon white-lipped python
- Liasis
    - Liasis fuscus, Brown water python
    - Liasis mackloti, Macklot's python
    - Liasis mackloti mackloti, Macklot's python
    - Liasis mackloti savuensis, Savu python
    - Liasis olivaceus, Olive python
    - Liasis olivaceus barroni, Pilbara olive python
    - Liasis olivaceus olivaceus, Olive python
- Morelia
    - Morelia amethistina, Amethystine python
    - Morelia clastolepis, Moluccan Python
    - Morelia boeleni, Boelen's python
    - Morelia bredli, Bredl's python
    - Morelia carinata, Rough-scaled python
    - Morelia kinghorni, Kinghorn's python
    - Morelia nauta, Tanimbar python
    - Morelia oenpelliensis, Oenpelli python
    - Morelia spilota, Carpet pythons
    - Moreli a spilota cheynei, Jungle carpet python
    - Morelia spilota imbricata, Southwestern carpet python
    - Morelia spilota mcdowelli, Coastal carpet python
    - Morelia spilota metcalfei, Inland carpet python
    - Morelia spilota spilota, Diamond python
    - Morelia spilota variegata, Northwestern carpet python
    - Morelia tracyae, Halmahera python
    - Morelia viridis, Green tree python
- Python, Pythons
    - Python anchietae, Angolan python
    - Python bivittatus, Burmese python
    - Python bivittatus progschai, Dwarf Burmese python
    - Python breitensteini, Borneo short-tailed python
    - Python brongersmai, Red blood python
    - Python curtus, Sumatran short-tailed python
    - Python kyaiktiyo, Myanmar short-tailed python
    - Python molurus, Indian python
    - Python molurus molurus, Indian python
    - Python regius, Royal python
    - Python reticulatus, Reticulated python
    - Python sebae, African rock python
    - Python sebae natalensis, Natal rock python
    - Python sebae sebae, African rock python
    - Python timoriensis, Timor python