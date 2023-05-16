from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post-detail/<int:id>/', views.post_detail, name='post-detail'),
]