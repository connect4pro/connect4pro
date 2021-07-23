from django.urls import path
from django.views.decorators.http import require_POST
from events.views import EventList, EventCommentsList, EventCommentCreate, EventDetail

app_name = 'events'

urlpatterns = [
    path('api/events', EventList.as_view(), name = 'events'),
    path('api/events/detail/<id>', EventDetail.as_view(), name = 'event_create'),
    path('api/events/comments', EventCommentsList.as_view(), name = 'event_comments'),
    path('api/events/comments/create_comment', EventCommentCreate.as_view(), name = 'event_comments_create'),
]