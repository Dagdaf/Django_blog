from django.urls import path
from blog.views import *

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/draft/', post_draft, name='post_draft'),
    path('post/recommends/', recommends, name='recommends'),
    path('post/category_posts/<int:category_pk>', category_posts, name='category_posts'),
    path('post/detail/<int:post_pk>', post_detail, name='post_detail'),
    path('post/published/<int:post_pk>', published_post, name='published_post'),
    path('post/edit/<int:post_pk>', post_edit, name='post_edit'),
    path('post/delete/<int:post_pk>', post_delete, name='post_delete'),
    path('post/comment_delete/<int:post_pk>/<int:comment_pk>', comment_delete, name='comment_delete'),
    path('post/new/', post_new, name='post_new'),
]
