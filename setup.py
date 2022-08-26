import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sssoon',
    version='0.1.8',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A simple Django app to add a beautiful coming soon page to your project.',
    long_description=README,
    url='https://github.com/KINGH242/django-sssoon',
    author='Kingpin Apps',
    author_email='hadderley@kingpinapps.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2.15',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=[
        'Django>=3.2.15',
        'django-recaptcha>=3.0.0',
    ],
)
