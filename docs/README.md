Documentation

Django-sssoon is a simple Django app to add beautiful coming soon webpage to your django website. This template is
based on on Bootstrap 3 and designed by Bootstrapious.com.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "sssoon" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'captcha',
        'sssoon',
    ]

2. Include the sssoon URLconf in your project urls.py like this to make your index page coming sssoon::

    path('', include('sssoon.urls', namespace="sssoon")),


3. Collect static files

    python manage.py collectstatic

4. Start the development server and visit http://127.0.0.1:8000/
