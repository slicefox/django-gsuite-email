=====
GSuite Email Backend
=====

This package helps send emails through google GSuite serviceaccount credentials

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