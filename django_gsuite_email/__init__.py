from .backends import GSuiteEmailBackend
from .utils import check_ready

# check if app is usable, raises improperly configured, if not ready
check_ready()

default_app_config = 'django_gsuite_email.apps.DjangoGSuiteEmailConfig'
