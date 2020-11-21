.. Django GSuite Email documentation master file, created by
   sphinx-quickstart on Thu Nov 12 13:32:18 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django GSuite Email's documentation!
===============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


This package allows to use Django's `send_mail` command to send emails through GSuite account.

It requires a serviceaccount credential created in Google coud console,
The crendential file need to have *https://www.googleapis.com/auth/gmail.send* scope.

Follow `this tutorial <https://developers.google.com/identity/protocols/oauth2/service-account#python>`_  to create the credentials file, make sure to add `https://www.googleapis.com/auth/gmail.send` scope.




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



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
