# -*- coding: utf-8 -*-
import os
import tempfile

SECRET_KEY = "x"


INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "easy_thumbnails",
    "filer",
    "shuup.admin",
    "shuup.core",
    "shuup.customer_group_pricing",
    "shuup.campaigns",
    "shuup.front",
    "shuup.default_tax",
    "shuup_stripe",
    "shuup.testing",
    "shuup.notify",
    "bootstrap3"
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(
            tempfile.gettempdir(),
            'shuup_stripe_tests.sqlite3'
        ),
    }
}
ROOT_URLCONF = 'shuup_workbench.urls'

class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"


MIGRATION_MODULES = DisableMigrations()
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "var", "media")

LANGUAGES = [
    ('en', 'English'),
    ('fi', 'Finnish'),
    ('ja', 'Japanese'),
    ('zh-hans', 'Simplified Chinese'),
    ('pt-br', 'Portuguese (Brazil)'),
]

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
