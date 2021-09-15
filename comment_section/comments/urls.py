from django.urls import path
from . import views

urlpatterns = [
    path('comments/', views.Commentlist.as_view()),
    path('comments/<int:pk>/', views.Commentdetail.as_view()),
    path('reply/', views.Replylist.as_view()),
    path('reply/<int:pk>/', views.Replydetail.as_view())   
]