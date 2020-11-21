# GSuite Email Backend

[![Downloads](https://static.pepy.tech/personalized-badge/django-gsuite-email?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/django-gsuite-email)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/slicefox/django-gsuite-email?color=brightgreen)
![GitHub issues](https://img.shields.io/github/issues/slicefox/django-gsuite-email)
[![Documentation Status](https://readthedocs.org/projects/django-gsuite-email/badge/?version=latest)](https://django-gsuite-email.readthedocs.io/en/latest/?badge=latest)

This package allows to use Django's `send_mail` command to send emails through GSuite account.

It requires a serviceaccount credential created in Google coud console,
The crendential file need to have `https://www.googleapis.com/auth/gmail.send` scope.

Follow [this tutorial](https://developers.google.com/identity/protocols/oauth2/service-account#python) to create the credentials file, make sure to add `https://www.googleapis.com/auth/gmail.send` scope.


## Installation
```sh
pip install django-gsuite-email
```

# Quick start

1. Add it to installed apps in `setings.py`
```python
INSTALLED_APPS = [
    ...
    'django_gsuite_email',
    ...
]
```
2. Set the Email EMAIL_BACKEND setting
```python
EMAIL_BACKEND = 'django_gsuite_email.GSuiteEmailBackend'
```
