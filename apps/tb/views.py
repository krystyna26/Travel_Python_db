from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request,"tb/index.html")

def logout(request):
    context = {
        "logout" : request.session.pop("user_id")
        }
    return render(request, "tb/index.html", context)

def login(request):
    result = User.objects.login_validator(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err,)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/welcome')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) == 0:
        password = request.POST['password']
        hashed = bcrypt.hashpw((password.encode()), bcrypt.gensalt(5))
        u = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=hashed
            )
        request.session['user_id'] = u.id
        messages.success(request, "Successfully registered!")
        return redirect('/welcome')
    else:
        for err in errors:
            messages.error(request, err)
            return redirect('/')

def welcome(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    # read
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'joined_trip' : Trip.objects.filter(joined_by=user), 
        'other_trip': Trip.objects.exclude(joined_by=user),
    }
    print Trip.objects.filter(joined_by=user) 
    return render(request, "tb/welcome.html", context)


def addTravel(request):
    return render(request, "tb/addTravel.html")
    
def add(request):
    error = Trip.objects.trip_validator(request.POST)
    if type(error) == list:
        for err in error:
            messages.error(request, err)
        return redirect('/welcome')
    messages.success(request, "Successfully added trip!")
    user = User.objects.get(id=request.session['user_id'])
    # create
    trip = Trip.objects.create(
        destination = request.POST['destination'],
        desc = request.POST['desc'],
        added_by = user,
        dateFrom = request.POST['dateFrom'],
        dateTo = request.POST['to']
    )
    u = User.objects.get(id=request.session['user_id'])
    trip.joined_by.add(u)
    return redirect('/welcome') 


def join(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    u = User.objects.get(id=request.session['user_id'])
    trip.joined_by.add(u)
    return redirect("/welcome")

