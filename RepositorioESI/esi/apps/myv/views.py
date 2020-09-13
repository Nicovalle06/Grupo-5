from django.shortcuts import render
from .models import Mito, Verdad


# Create your views here.
def MyV(request):
	return render(request,'myv/mitos.html')