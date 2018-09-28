from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='post_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)