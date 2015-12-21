from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
import sqlite3
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect

def mysearch (request):
    if request.method == "GET":
        return render(request, 'webapp.html', {})


