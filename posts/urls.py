from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('posts/<int:id>/', views.post_detail, name = 'post_detail'),
    path('create_post/', views.create_post, name = 'create_post'),
    path('delete_post/<int:pk>', views.delete_post, name='delete_post'),

]