from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from datetime import date, datetime
from django.contrib.auth import authenticate, login, logout

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib

subject = "Testmail" 
body = "Dies ist nur ein Test"
sender = "todo@mainguy.de"
recipient = "nikitametzger1430@gmail.com"
password = ""

# Create your views here.

### Mailfunction
def send_mail(subject, body, sender, recipient):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    text_part = MIMEText(body)
    msg.attach(text_part)

    with smtplib.SMTP_SSL('mail.mainguy.de', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, msg.as_string())
        print("Message sent!")


def redirect_homepage(request):
    return redirect('homepage')


### Login + Logout Start
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('homepage')
        else:
            messages.error(request, 'Login failed')
            return redirect('loginpage')
    return render(request, 'loginpage.html', {})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logout successful')
        return redirect('loginpage')
    else:
        return redirect('loginpage')
### Login + Logout End



def homepage(request):
    if request.user.is_authenticated:
        #send_mail(subject, body, sender, recipient)
        return render(request, 'homepage.html', {})
    else:
        return redirect('loginpage')