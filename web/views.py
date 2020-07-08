from django.shortcuts import render
from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import poster , news , client , subscribed
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime , timedelta
from django.db.models import Q
#from django.db.signals import post_save
from django.dispatch import receiver
import smtplib, ssl
# Create your views here.

@csrf_exempt
def home(request):
    return render (request , 'login.html')

@csrf_exempt
def panel(request):
    client_id = request.POST['clientid']
    cli = client.objects.get(token=client_id)
    if cli is not None :  
        now = datetime.now()
        posters = poster.objects.filter(clients = cli , timetolive__gte=now )
        akhbar = news.objects.filter(clients = cli  , TTL__gte=now)
        con={'posters' : posters  , 'akhbar' : akhbar}
        return render(request ,'panel.html' , con)
    else:
        return render (request , 'login.html')



"""@receiver(post_save, sender=news)
def send_mail_sms(sender, **kwargs):
    sub = subscribed.objects.all()
    masse=news.objects.latest('date_added')
    for ii in sub :‌
        email_send(ii.email , masse.text)




def email_send(reci , tex)
    port = 587  # For starttls
    smtp_server = ""
    sender_email = ""
    receiver_email = reci
    password = ""
    message =  tex

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        """
