from django.urls import path
from . import views

urlpatterns = [
    path('reply/', views.PostReply.as_view()),
    path('reply/<int:comment_id>/', views.ReplyList.as_view()),
]