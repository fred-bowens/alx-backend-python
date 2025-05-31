 
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install django djangorestframework


django-admin startproject messaging_app
cd messaging_app



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
    'rest_framework',

    
    'chats',
]

t
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}

python manage.py migrate

python manage.py runserver


