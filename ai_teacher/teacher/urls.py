from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_style, name='select_style'),
    path('chat/<int:style_id>/', views.chat_view, name='chat'),
    path('ask/<int:style_id>/', views.ask_ai, name='ask_ai'),
]