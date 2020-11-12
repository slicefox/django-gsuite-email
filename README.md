# GSuite Email Backend

[![Downloads](https://static.pepy.tech/personalized-badge/django-gsuite-email?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/django-gsuite-email)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/slicefox/django-gsuite-email?logoColor=red)
![GitHub issues](https://img.shields.io/github/issues/slicefox/django-gsuite-email)
[![Documentation Status](https://readthedocs.org/projects/django-gsuite-email/badge/?version=latest)](https://django-gsuite-email.readthedocs.io/en/latest/?badge=latest)

This package helps send emails through google GSuite serviceaccount credentials


## Installation

pip install django-gsuite-email


# Quick start

1. Add this to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_gsuite_email',
        ...
    ]

2. Set the Email EMAIL_BACKEND setting in settings like this::

    EMAIL_BACKEND = 'django_gsuite_email.GSuiteEmailBackend'