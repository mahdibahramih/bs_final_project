from django.shortcuts import render
from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import poster , news , client
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime , timedelta
# Create your views here.

@csrf_exempt
def home(request):
    return render (request , 'login.html')

@csrf_exempt
def panel(request):
    client_id = request.POST['clientid']
    cli = client.objects.get(token=client_id)
    if cli is not None :  
        posters = poster.objects.filter(clients = cli)
        akhbar = news.objects.filter(clients = cli)
        con={'posters' : posters  , 'akhbar' : akhbar}
        return render(request ,'panel.html' , con)
    else:
        return render (request , 'login.html')