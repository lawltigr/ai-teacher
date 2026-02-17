from django.shortcuts import render
from .models import TeachingStyle

def select_style(request):
    styles = TeachingStyle.objects.all()
    return render(request, 'select_style.html', {'styles': styles})

# Create your views here.
