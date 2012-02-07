### -*- coding: utf-8 -*- ####################################################
#
# Copyright (c) 20011 max38934. All Rights Reserved.
#
##############################################################################

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

install_requires = [
        'setuptools',
        'Django',
        'django-registration',
        'django-social-auth',
#        'django-mptt >= 0.4.0',
#        'django-uni-form',
#        'sorl-thumbnail',
        'South',
#        'sorl',
        'PIL',
#        'Fabric',
        'django-pagination',
        'cElementTree'
#        'ElementTree'
#        'simplejson',
#        'httplib2',
#        'lxml',
#        'django-rosetta',
#        #'django-tinymce',
#        'django-simple-captcha',
#        'pycrypto >= 2.1',
#        'oauth',
#        'celery',
#        'django-celery',
#        'django-kombu',
#        'python-openid',
#        "django-tagging",
#        "django_concurrent_test_server",
]

extras_require = dict(
    test = [
        'coverage',
        'windmill',
    ]
)

#AFAIK:
install_requires.extend(extras_require['test'])


dependency_links = [
        'http://dist.repoze.org',
        'http://pypi.pinaxproject.com/',
        'http://distfiles.minitage.org/public/externals/minitage/',
]

setup(name="project_task",
            version="0.1",
            description="task",
            author="roman",
            packages = find_packages('src'),
            package_dir = {'': 'src'},
            include_package_data = True,
            zip_safe = False,
            install_requires = install_requires,
            extras_require = extras_require,
            entry_points="""
              # -*- Entry points: -*-
              """,
            dependency_links = dependency_links,
)
