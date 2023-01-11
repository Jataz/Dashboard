from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import VehiclesForm
from base.models import Vehicle

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect("login")


def dashboard(request):
     return render(request,'dashboard.html')

def users(request):
    user = User.objects.all()
    context = {'user':user}

    return render(request,'users.html',context)

def createUser(request):

    if request.method == 'POST':
        owner = request.POST.get('owner')
        license_number = request.POST.get('license_number')
        mobile_number = request.POST.get('mobile_number')
        model = request.POST.get('model')
        role = request.POST.get('role')
        status = request.POST.get('status')

        vehicle = Vehicle(
            owner = owner,
            license_number = license_number,
            mobile_number = mobile_number,
            model = model,
            role = role,
            status = status

        )

        vehicle.save()
        return redirect('users')

    return render(request,'users.html')

def updateUser(request,id):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')

        user = User(
            id = id,
            first_name = first_name,
            last_name  = last_name ,
            username = username,
            email = email,
        )

        user.save()
        return redirect('users')

    return render(request,'users.html')

def userPassword(PasswordChangeView):
    
    template_name = 'change_passowrd.html'
    success_url = reverse_lazy()

def vehicles(request):

    vehicle = Vehicle.objects.all()
    context = {'vehicle':vehicle} 

    return render(request,'vehicles.html',context)

def createVehicle(request):

    if request.method == 'POST':
        owner = request.POST.get('owner')
        license_number = request.POST.get('license_number')
        mobile_number = request.POST.get('mobile_number')
        model = request.POST.get('model')
        role = request.POST.get('role')
        status = request.POST.get('status')

        vehicle = Vehicle(
            owner = owner,
            license_number = license_number,
            mobile_number = mobile_number,
            model = model,
            role = role,
            status = status

        )

        vehicle.save()
        return redirect('vehicles')

    return render(request,'vehicles.html')

def viewVehicle(request):

    vehicle = Vehicle.objects.all()
    context = {'vehicle':vehicle}

    return render(request,'vehicles.html',context)

def updateVehicle(request,id):

    if request.method == 'POST':
        owner = request.POST.get('owner')
        license_number = request.POST.get('license_number')
        mobile_number = request.POST.get('mobile_number')
        model = request.POST.get('model')
        role = request.POST.get('role')
        status = request.POST.get('status')

        vehicle = Vehicle(
            id = id,
            owner = owner,
            license_number = license_number,
            mobile_number = mobile_number,
            model = model,
            role = role,
            status = status

        )

        vehicle.save()
        return redirect('vehicles')

    return render(request,'vehicles.html')

def deleteVehicle(request,id):

    row = Vehicle.objects.filter(id=id)
    row.delete()

    context = {"row":row}
    return redirect('vehicles')