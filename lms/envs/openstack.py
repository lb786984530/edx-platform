"""
Settings for OpenStack deployments.
"""

# We import the aws settings because that's currently where the base settings are stored for all deployments.
# TODO - fix this when aws.py is split/renamed.
from .aws import *  # pylint: disable=wildcard-import, unused-wildcard-import

SWIFT_AUTH_URL = AUTH_TOKENS.get('SWIFT_AUTH_URL')
SWIFT_AUTH_VERSION = AUTH_TOKENS.get('SWIFT_AUTH_VERSION', 1)
SWIFT_USERNAME = AUTH_TOKENS.get('SWIFT_USERNAME')
SWIFT_KEY = AUTH_TOKENS.get('SWIFT_KEY')
SWIFT_TENANT_NAME = AUTH_TOKENS.get('SWIFT_TENANT_NAME')
SWIFT_TENANT_ID = AUTH_TOKENS.get('SWIFT_TENANT_ID')
SWIFT_CONTAINER_NAME = FILE_UPLOAD_STORAGE_BUCKET_NAME
SWIFT_NAME_PREFIX = FILE_UPLOAD_STORAGE_PREFIX
SWIFT_USE_TEMP_URLS = AUTH_TOKENS.get('SWIFT_USE_TEMP_URLS', False)
SWIFT_TEMP_URL_KEY = AUTH_TOKENS.get('SWIFT_TEMP_URL_KEY')
SWIFT_TEMP_URL_DURATION = AUTH_TOKENS.get('SWIFT_TEMP_URL_DURATION', 1800)  # seconds
SWIFT_CONTENT_TYPE_FROM_FD = AUTH_TOKENS.get('SWIFT_CONTENT_TYPE_FROM_FD', True)
SWIFT_CONTENT_LENGTH_FROM_FD = AUTH_TOKENS.get('SWIFT_CONTENT_LENGTH_FROM_FD', False)
SWIFT_LAZY_CONNECT = AUTH_TOKENS.get('SWIFT_LAZY_CONNECT', True)

if AUTH_TOKENS.get('SWIFT_REGION_NAME'):
    SWIFT_EXTRA_OPTIONS = {'region_name': AUTH_TOKENS['SWIFT_REGION_NAME']}

if AUTH_TOKENS.get('DEFAULT_FILE_STORAGE'):
    DEFAULT_FILE_STORAGE = AUTH_TOKENS.get('DEFAULT_FILE_STORAGE')
elif SWIFT_AUTH_URL and SWIFT_USERNAME and SWIFT_KEY:
    DEFAULT_FILE_STORAGE = 'swift.storage.SwiftStorage'
else:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

ORA2_FILEUPLOAD_BACKEND = "django"
