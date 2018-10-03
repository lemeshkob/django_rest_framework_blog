from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Blog API')


urlpatterns = [
    path('api-root/', views.api_root),
    path('schema/', schema_view),
    path('', views.posts_view),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name='comment-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
