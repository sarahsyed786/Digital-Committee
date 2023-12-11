
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from requests import request
from django.contrib.auth.forms import UserCreationForm
from project import settings
from django.core.mail import send_mail

# Create your views here.



def home(request):
    return render(request, "fair_collection/index.html" )

def signup(request):
    if request.method ==    'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']

        # Validations
        if User.objects.filter(username=username):
            messages.error(request, 'User name already exist! Please try some other user name. ')
            return redirect('/signup')
        
        if User.objects.filter(email=email):
            messages.error(request,'Email already registered!')
            return redirect('/signup')
        
        if len(username)>10:
            messages.error(request,'Username must be under 10 characters.')
            return redirect('/signup')

        if len(username)<5:
            messages.error(request,' Username must have atleast 5 characters ')
            return redirect('/signup')
        
        if password!=cpass:
            messages.error(request,"Password didn't match!")
            return redirect('/signup')
        
        if not username.isalnum():
            messages.error(request,'Username must contain alphabats and numbers and no special charachers in it')
            return redirect('/signup')


        myuser = User.objects.create_user(username, email, password) #Create user 
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.address1 = address

        myuser.save() #save users data
        messages.success(request, "Your Account has been successfully created.")

        return redirect('/signin') 


    return render(request, "fair_collection/signup.html" )

def signin(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.username
            return render(request, "fair_collection/index.html", {'fname':fname} )

        else:
            messages.error(request, "Bad Credential")
            return redirect("home")



    return render(request, "fair_collection/signin.html" )



def signout(request):
   logout(request)
   messages.success(request, "Logged Out Successfully!")
   return redirect("home")

def features(request):
        
        return render(request, "fair_collection/features.html" )

def about(request):
    return render(request, "fair_collection/about.html" )

