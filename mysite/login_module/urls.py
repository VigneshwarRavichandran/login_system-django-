from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('welcome/', views.welcome, name = 'welcome'),
	path('<int:user_id>/results/', views.results, name = 'results'),
]