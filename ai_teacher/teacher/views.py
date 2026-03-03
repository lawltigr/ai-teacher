from django.shortcuts import render, get_object_or_404
from .models import TeachingStyle
from django.http import JsonResponse
import json
from .ai_service import generate_answer
from django.views.decorators.csrf import csrf_exempt

def select_style(request):
    styles = TeachingStyle.objects.all()
    return render(request, 'select_style.html', {'styles': styles})

def chat_view(request, style_id):
    style = get_object_or_404(TeachingStyle, id=style_id)
    return render(request, 'chat.html', {'style': style})


@csrf_exempt
def ask_ai(request, style_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message")
            style = TeachingStyle.objects.get(id=style_id)
            ai_response = generate_answer(style, user_message)
            return JsonResponse({"answer": ai_response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
