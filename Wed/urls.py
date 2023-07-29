from django.urls import path
from . import views 

urlpatterns = [
    path('', views.homepage, name='index'),
    path('story/', views.story, name='story'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('single_blog/', views.single_blog, name='single_blog'),
    path('accommodation/', views.accommodation, name='accommodation'),
    path('elements/', views.elements, name='elements'),
    path('contact/', views.contact, name='contact'),
]