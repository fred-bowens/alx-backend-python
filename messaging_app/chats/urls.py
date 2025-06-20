from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet, basename='conversations')
router.register(r'messages', MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]
This will automatically create routes like:

GET /api/conversations/ – list all conversations

POST /api/conversations/ – create a new conversation

GET /api/conversations/{id}/ – get a specific conversation

POST /api/conversations/{id}/send_message/ – custom action to send a message

GET /api/messages/ – list all messages

GET /api/messages/{id}/ – get a single message

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),  
]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chats.views import ConversationViewSet, MessageViewSet

router = DefaultRouter()

router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the router-generated URLs under the 'api/' path
]
