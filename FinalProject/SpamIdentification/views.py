from django.shortcuts import render

# Create your views here.

def home(request):
	#logic for view
	return render(request,'SpamIdentification/home.html',)
