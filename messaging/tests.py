python manage.py shell
from django.contrib.auth.models import User
from messaging.models import Message, Notification

alice = User.objects.create_user(username='alice', password='pass')
bob = User.objects.create_user(username='bob', password='pass')


msg = Message.objects.create(sender=alice, receiver=bob, content="Hello Bob!")


Notification.objects.filter(user=bob).exists()
