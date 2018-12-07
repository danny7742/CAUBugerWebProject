from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from .models import User, Menu, Seat, Order, Notice
from .forms import LoginForm

#Main Page
def index(request):
    template = loader.get_template('mycontact/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

#Introduction Page
def introduction(request):
    template = loader.get_template('mycontact/introduction.html')
    contacts = Menu.objects.order_by('pk')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))

#Order Page
def order(request):
    template = loader.get_template('mycontact/order.html')
    contacts = Order.objects.order_by('pk')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))

#Seat Page
def seats(request):
    template = loader.get_template('mycontact/seats.html')
    contacts = Seat.objects.order_by('pk')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))

#Notice Page
def notice(request):
    template = loader.get_template('mycontact/notice.html')
    contacts = Notice.objects.order_by('pk')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))

#Insert Page
def login(request):
    #new form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = LoginForm()

    template = loader.get_template('mycontact/login.html')
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context, request))

#Signup Page
def signup(request):
    template = loader.get_template('mycontact/signup.html')
    contacts = User.objects.order_by('pk')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))

#Search PW Page
def searchpw(request):
    template = loader.get_template('mycontact/searchpw.html')
    contacts = User.objects.order_by('pk')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))

#Change PW Page
def changepw(request):
    template = loader.get_template('mycontact/changepw.html')
    contacts = User.objects.order_by('pk')
    context = {
        'contacts' : contacts
    }
    return HttpResponse(template.render(context, request))
