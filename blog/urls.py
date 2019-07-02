from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail')
]