from django.shortcuts import render
from home.models import Historial_medico
from home.models import Recien_nacido

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def login(request):
    return render(request, 'home/login.html')