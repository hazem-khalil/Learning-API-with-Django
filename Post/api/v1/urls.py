from django.urls import path
from .views import api_detail_post_view, api_posts_view

urlpatterns = [
    path('', api_posts_view),
    path('<title>/', api_detail_post_view),
]