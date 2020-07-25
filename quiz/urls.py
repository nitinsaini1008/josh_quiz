from django.urls import path,include
from .import views

urlpatterns = [
	path('',views.home,name='home'),
	path('about',views.about,name='about'),
	path('test',views.test,name='test'),
	path('user_login',views.user_login,name='user_login'),
	path('result',views.result,name='result'),
]
