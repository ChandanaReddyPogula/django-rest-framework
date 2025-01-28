from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    #path('postList/', views.PostList.as_view(), name='postList'),
    #path('postDetail/<int:post_id>/', views.PostDetail.as_view(), name='postDetail'),
]

"""
    path('all-posts/', views.all_posts, name='all-posts'),
    path('get-post/<int:post_id>/', views.get_post, name='get_post'),
    path('add-post/', views.add_post, name='add_post'),
    path('update-post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
"""
