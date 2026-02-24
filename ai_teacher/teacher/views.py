from django.shortcuts import render, get_object_or_404
from .models import TeachingStyle

def select_style(request):
    styles = TeachingStyle.objects.all()
    return render(request, 'select_style.html', {'styles': styles})

def chat_view(request, style_id):
    style = get_object_or_404(TeachingStyle, id=style_id)
    return render(request, 'chat.html', {'style': style})

# Create your views here.
