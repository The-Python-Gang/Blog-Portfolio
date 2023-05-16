from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post-detail/<int:id>/', views.post_detail, name='post-detail'),
    path('devs/', views.devs, name='devs'),
    path('dev-id/<int:id>/', views.dev_id, name='dev-id'),
]