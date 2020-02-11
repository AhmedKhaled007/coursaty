from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    # url(r'^$', views.all_posts,name='all_posts'),
    # url(r'^(?P<id>\d+)$', views.post,name='post'),
    # # path('comment/<int:id>/', views.comment, name='comment'),
    # url(r'^create', views.create_post,name='create_post'),
    # url(r'^(?P<id>\d+)/edit$', views.edit_post,name='edit_post'),
    # url(r'^comment/(?P<id>\d+)$', views.comment,name='comment'),

    path('', views.all_posts,name='all_posts'),
    path('<int:id>/', views.post, name='post'),
    path('create/', views.create_post, name='createpost'),
    path('<int:id>/edit/', views.edit_post, name='edit_post'),
    path('comment/<int:id>', views.comment, name='comment')
]
