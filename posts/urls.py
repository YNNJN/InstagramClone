from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('hashtags/<int:post_id>/', views.hashtags, name="hashtags"),
    path('<int:post_id>/', views.detail, name="detail"),
    path('<int:post_id>/like/', views.like, name="like"),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/update/', views.update, name="update"),
    path('<int:post_id>/comment_create/', views.comment_create, name="comment_create"),
    path('<int:post_id>/comment_delete/', views.comment_delete, name="comment_delete"),
]