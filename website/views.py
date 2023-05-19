from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template import loader
from django.utils import timezone
from .forms import SignUpForm, adicionarForm
from .models import Record

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

def logout_user(request):
   logout(request)
   messages.success(request, "deslogou")
   return redirect('home')

def musculo(request):
   messages.success(request, "página musculo")
   return render(request, "musculo.html")

def laminas(request):
   messages.success(request, "página laminas")

   #import models record
   records = Record.objects.all()
   return render(request, "laminas.html",{'records':records})




def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
           form.save()
           #autenticar e logar
           username = form.cleaned_data['username']
           password = form.cleaned_data['password1']
           user = authenticate(username=username, password=password)
           login(request, user)
           messages.success(request, "você logou")
           return redirect('home')
    else:
        form = SignUpForm()

        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})


def customer_record(request, pk):

   if request.user.is_authenticated:
      customer_record = Record.objects.get(id=pk)
      return render(request, 'record.html', {'customer_record':customer_record})

   else:
      messages.success(request, "deve estar logado")
      return redirect('home')

      
      today = timezone.now()
      return render(request, "home.html", {"today" : today})
def adicionar(request):

   form = adicionarForm(request.POST or None)

   if request.user.is_authenticated:
      if request.method == "POST":
         if form.is_valid():
            adicionar = form.save()
            messages.success(request, "Adicionado")
            return redirect('home') 
     # customer_record = Record.objects.get(id=pk)
      return render(request, 'adicionar.html',{'form':form})
                    #, {'customer_record':customer_record})

   else:
      messages.success(request, "deve estar logado")
      return redirect('home')
   

def sala(request):
   messages.success(request, "sala")
   return render(request, "sala.html")

def room(request,room_name):
   return render(request, 'chatroom.html',{
         'room_name':room_name
   })