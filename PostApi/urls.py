from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from Post.api.v1.views import PostList
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/posts/$', PostList.as_view()),
    path('api/posts/', include('Post.api.v1.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]