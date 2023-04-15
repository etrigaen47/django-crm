from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    #check to see if user is logging in
    
    ##when user is logging in, they are POSTing, else they are 
    ##GETting the request instaead of POSTing
    
    if request.method == 'POST':
        u_name = request.POST['username'] 
        u_pass = request.POST['password']
        
        #Authenticate
        user = authenticate(request, username=u_name, password=u_pass)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been successfully logged in, Master {}!'.format(user))
            return redirect('home')
        else:
            messages.success(request, 'Error logging in, try again...')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})


def logout_user(request):
    #in built django message
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Log In
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been registered successfully!')
            return redirect('home')
    else:
        # we dont pass in any request to the SignUpForm 
        # because the user has not yet filled out the form
        # unllike the instance above which is for when they 
        # fill out the form
        form = SignUpForm()
        # here, your form will be passed into the register.html page
        # and then we can do something with it
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
    #pk is primary ke that we set in the urls page
    if request.user.is_authenticated:
        #look up records
        # Record.objects.get -> gets the record of a single record in the db
        # id comes from out migration in n from the db
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, 'You must be logged in to view that page!')
        return redirect('home')
    
def delete_customer(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        
        messages.success(request, 'Record deleted successfully!')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in to delete records!')
        return redirect('home')
    
def add_customer(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid:
                add_record = form.save()
                messages.success(request, 'Record added successfully!')
                return redirect('home')
            # in case they are not POSTing rn
        return render(request, "add_record.html", {"form":form})
    else:
        messages.success(request, 'You must be logged in to add records!')
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        # here we call the add record form but then we now get the full 
        # data of the record we want to update and then pass that as an 
        # instance to propagate the add record form
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record has been updated!')
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in to edit records!')
        return render('home')
                