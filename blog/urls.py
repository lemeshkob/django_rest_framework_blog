from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Blog API')


urlpatterns = [
    path('api-root/', views.api_root, name='home'),
    path('schema/', schema_view),
    path('', views.PostList.as_view(), name='post-list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
