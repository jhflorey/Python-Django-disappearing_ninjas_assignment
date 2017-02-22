from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
	context = {"no": True}
	return render(request, 'disappearingninjas/index.html', context)
	
def ninjas(request):	
	return render(request, 'disappearingninjas/ninjas.html')

def color(request, color):
	turtle_option = {
		'blue': 'disappearingninjas/images/leo.jpg',
		'red': 'disappearingninjas/images/raphael.png',
		'orange': 'disappearingninjas/images/michel.gif',
		'purple': 'disappearingninjas/images/donatello.gif',
	}
	if color in turtle_option:
		context = {
			'image':turtle_option[color]
		}
	else:
		context = {
			'image':'disappearingninjas/images/meganfox.jpeg',
		}
	return render(request, 'disappearingninjas/index.html', context)

