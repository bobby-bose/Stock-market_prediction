from app.models import UserResponse

import json

from django.shortcuts import render
def index(request):
    return render(request, 'index.html')


investment_amount = 0
risk_amount = 0

import json
from django.shortcuts import render


import json
from django.shortcuts import render, redirect



def chat_board(request):
    if request.method == "POST":
        try:
            
def chatbot_next(request, message):
    return render(request, "chat_board.html", {"message": message})







def analytical_part(request):
    return render(request, 'analytical_part.html')
