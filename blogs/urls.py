from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name="index"),
    path('list/all', views.list_all, name='list_all'),
    path('list/my', views.my_posts, name='my_posts'),
    path('post/new', views.new_post, name='new_post'),
    path('post/<int:post_id>', views.post, name='post'),
    path('post/<int:post_id>/delete', views.delete, name='delete'),
    path('post/<int:post_id>/edit', views.edit_post, name='edit_post'),
]
