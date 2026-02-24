from django.shortcuts import render, get_object_or_404
from .models import TeachingStyle
from django.http import JsonResponse
import json

def select_style(request):
    styles = TeachingStyle.objects.all()
    return render(request, 'select_style.html', {'styles': styles})

def chat_view(request, style_id):
    style = get_object_or_404(TeachingStyle, id=style_id)
    return render(request, 'chat.html', {'style': style})

def ask_ai(request, style_id):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")
        style = TeachingStyle.objects.get(id=style_id)
        ai_response = f"{style.name} answers: {user_message}"
        return JsonResponse({"answer": ai_response})
