AUTH_USER_MODEL = 'chats.User'

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
python manage.py makemigrations
python manage.py migrate

from .models import User

from django.contrib.auth.models import User  
Watching for file changes with StatReloader
Performing system checks...
