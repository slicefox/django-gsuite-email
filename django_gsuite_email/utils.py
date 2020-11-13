from django.conf import settings
import sys
from os import path,  environ
from django.core.exceptions import ImproperlyConfigured

# will be in this format (Major,Minor,) ex (3,6,) 
PYTHON_VERSION = sys.version_info[0:2]

def check_file(file_path):
    # check if file_path exists
    if not  path.exists(file_path):
        raise ImproperlyConfigured('Credentials file not found at %s'%(file_path))
    # check if file_path is actually file, not directory
    if not path.isfile(file_path):
        raise ImproperlyConfigured('%s is not a file'%(file_path))
    return True

def get_credentials_file():
    """Returns location of credentials file, from either environment variable or settings
    settings has precedance over environment variable
    """    
    if hasattr(settings, 'GSUITE_CREDENTIALS_FILE'):
        # 
        file_path = settings.GSUITE_CREDENTIALS_FILE
        if check_file(file_path):
            return file_path

    if environ.get('GSUITE_CREDENTIALS_FILE') is not None:
        file_path = environ.get('GSUITE_CREDENTIALS_FILE')
        if check_file(file_path):
            return file_path
    raise ImproperlyConfigured('GSUITE_CREDENTIALS_FILE is not set, set it in seetings or as environment variable')



def check_ready():
    return bool(get_credentials_file())