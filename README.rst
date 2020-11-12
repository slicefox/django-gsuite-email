====================
GSuite Email Backend
====================
.. image:: https://static.pepy.tech/personalized-badge/django-gsuite-email?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
 :target: https://pepy.tech/project/django-gsuite-email
.. image:: https://img.shields.io/github/v/release/slicefox/django-gsuite-email
.. image:: https://img.shields.io/github/issues/slicefox/django-gsuite-email

This package helps send emails through google GSuite serviceaccount credentials


Installation
------------

pip install django-gsuite-email


Quick start
-----------

1. Add this to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_gsuite_email',
        ...
    ]

2. Set the Email EMAIL_BACKEND setting in settings like this::

    EMAIL_BACKEND = 'django_gsuite_email.GSuiteEmailBackend'