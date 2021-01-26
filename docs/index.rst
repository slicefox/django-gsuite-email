.. Django GSuite Email documentation master file, created by
   sphinx-quickstart on Thu Nov 12 13:32:18 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django GSuite Email's documentation!
===============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Installing
----------
Install **Django GSuite Email** with

.. code-block:: bash

  pip install django-gsuite-email

Usage
-----
1. Add to installed apps in `setings.py`::

    INSTALLED_APPS = [
        ...
        'django_gsuite_email',
        ...
    ]

2. Set the Email EMAIL_BACKEND setting::

    EMAIL_BACKEND = 'django_gsuite_email.GSuiteEmailBackend'

3. Send emails::

    from django.core.mail import send_mail

    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
