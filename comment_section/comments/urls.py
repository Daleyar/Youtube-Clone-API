from django.urls import path
from . import views

urlpatterns = [
    path('comments/<str:videoId>/', views.CommentList.as_view()),
    path('post_comment/', views.PostCommment.as_view()),
    path('comments/like/<int:pk>/', views.LikeComment.as_view()),
    path('comments/dislike/<int:pk>/', views.DislikeComment.as_view())   
]