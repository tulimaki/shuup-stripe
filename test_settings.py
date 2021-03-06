# -*- coding: utf-8 -*-
# This file is part of Shuup Stripe Addon.
#
# Copyright (c) 2012-2018, Shuup Inc. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
import os
import tempfile

SECRET_KEY = "x"


INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "easy_thumbnails",
    "filer",
    "shuup.core",
    "shuup.admin",
    "shuup.customer_group_pricing",
    "shuup.campaigns",
    "shuup.front",
    "shuup.default_tax",
    "shuup.testing",
    "shuup.notify",
    "shuup_stripe",
    "bootstrap3",  # shuup.admin requirement
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(
            tempfile.gettempdir(),
            'tests.sqlite3'
        ),
    }
}


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"


MIGRATION_MODULES = DisableMigrations()
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "var", "media")

STATIC_URL = "static/"

ROOT_URLCONF = 'shuup_workbench.urls'

LANGUAGES = [
    ('en', 'English'),
    ('fi', 'Finnish'),
    ('ja', 'Japanese'),
    ('zh-hans', 'Simplified Chinese'),
    ('pt-br', 'Portuguese (Brazil)'),
]
USE_TZ = True

PARLER_DEFAULT_LANGUAGE_CODE = "en"

PARLER_LANGUAGES = {
    None: [{"code": c, "name": n} for (c, n) in LANGUAGES],
    'default': {
        'hide_untranslated': False,
    }
}

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".jinja",
            "newstyle_gettext": True,
        },
        "NAME": "jinja2",
    },
]

# This is being used the pull connect data from configuration
STRIPE_CONNECT_OAUTH_DATA_KEY = "stripe_connect_oauth_data"

# platform level secrets for connect to use
STRIPE_SECRET_KEY = "sk_test_aasdf"
STRIPE_PUBLIC_KEY = "sk_test_aasdf"
STRIPE_CONNECT_REDIRECT_URI = "https://www.stripe.com"
STRIPE_CONNECT_REDIRECT_ADMIN_URI = None
STRIPE_OAUTH_CLIENT_ID = "sk_test_aasdf"

STRIPE_CONNECT_FEE_PERCENTAGE = None

STRIPE_OAUTH_REDIRECTOR = "shuup_stripe.redirector:StripeRedirector"
