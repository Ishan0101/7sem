from django.urls import path
from . import views

app_name = 'SpamIdentification'

urlpatterns = [
	path('',views.home,name='home'),
]