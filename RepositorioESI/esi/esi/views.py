from django.shortcuts import render


def Home(request):
	print("HOLA")
	return render(request,'home.html')