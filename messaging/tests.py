python manage.py shell
from django.contrib.auth.models import User
from messaging.models import Message, Notification

alice = User.objects.create_user(username='alice', password='pass')
bob = User.objects.create_user(username='bob', password='pass')


msg = Message.objects.create(sender=alice, receiver=bob, content="Hello Bob!")


Notification.objects.filter(user=bob).exists()

from messaging.models import Message

msg = Message.objects.create(sender=alice, receiver=bob, content="Hello Bob!")
msg.content = "Hi Bob, how are you?"
msg.save()

msg.history.all().values('old_content', 'edited_at')
