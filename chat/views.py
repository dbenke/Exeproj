from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.utils import timezone


def home(request):


   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = authenticate(request, username=username, password=password)

       if user is not None:
         login(request, user)
         messages.success(request, "logou")
         return redirect('home')
       else:
         messages.success(request, "erroerro")
         return redirect('home')
   else:
      today = timezone.now()
     # template = loader.get_template("home.html")
   #return HttpResponse(text)
      return render(request, "home.html", {"today" : today})
      #return render(request, "home.html",{'records':records})

# Create your views here.

def sala(request):
   messages.success(request, "sala")
   return render(request, "sala.html")

def room(request,room_name):
   return render(request, 'chatroom.html',{
         'room_name':room_name
   })