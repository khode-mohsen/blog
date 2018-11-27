from django.urls import path
from .views import Home ,Detail,profile

urlpatterns=[
	path('',Home.as_view(),name='home'),
	path('blog/post/<int:pk>',Detail.as_view(),name='post_detail'),
	path('accounts/profile/',profile,name='profile')
	]