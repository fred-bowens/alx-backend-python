from django.shortcuts import render, get_object_or_404
from .models import Message


def message_detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    history = message.history.all().order_by('-edited_at')
    return render(request, 'messaging/message_detail.html', {
        'message': message,
        'history': history
    })  


def inbox_view(request):
    user = request.user
    unread_messages = Message.unread.for_user(user)
    return render(request, 'inbox.html', {'unread_messages': unread_messages})

from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from .models import Message, Conversation

@cache_page(60)  # Cache this view for 60 seconds
def conversation_detail(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    messages = Message.objects.filter(conversation=conversation).order_by('timestamp')
    return render(request, 'conversation_detail.html', {'conversation': conversation, 'messages': messages})
