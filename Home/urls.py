from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('p/<str:slug>/', views.post_view, name='post_view'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
