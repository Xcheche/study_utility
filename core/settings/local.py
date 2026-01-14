


from os import getenv
from .base import *  # noqa


# ========================================#
# Secret Key and Debug Configuration
# ========================================#

SECRET_KEY = getenv("SECRET_KEY", "unsafe-dev-key")

DEBUG = getenv("DEBUG", "False") == "True"


# ========================================#
# Hosts
# ========================================#

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]


# ========================================#
# Image Configuration
# ========================================#

MAX_UPLOAD_SIZE = 1 * 1024 * 1024  # 1 MB
