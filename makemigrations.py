#!/usr/bin/env python

import sys
import django

from django.conf import settings
from django.core.management import call_command

settings.configure(DEBUG=True,
    INSTALLED_APPS=(
        'django.contrib.contenttypes',
        'atlantisbot_api',
    ),
)

django.setup()
call_command('makemigrations', 'atlantisbot_api')
