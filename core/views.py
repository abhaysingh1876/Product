from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, EditProductForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from core.models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'core/home.html',{'products':products})



def dashboard(request):
    if request.user.is_authenticated:
        products = Product.objects.all()

        return render(request, 'core/dashboard.html', {'products': products})

    else:
        return HttpResponseRedirect('/login')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                passs = fm.cleaned_data['password']
                user = authenticate(username=uname, password=passs)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully...')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm()
        return render(request, 'core/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
    


def user_signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user=fm.save()
            messages.success(request, "User Registered Successfully....")
    else:
        fm = SignUpForm()
    return render(request, 'core/signup.html', {'form': fm})


def edit_product(request, id):
    if request.user.is_authenticated:
        udata = Product.objects.get(pk=id)
        if request.method == 'POST':
            fm = EditProductForm(instance=udata, data=request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Product Updated Successfully....')
                return HttpResponseRedirect('/dashboard')
        else:
            fm = EditProductForm(instance=udata)
            return render(request, 'core/editproduct.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def add_product(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditProductForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Product Added Successfully...')
                return HttpResponseRedirect('/dashboard')
            else:
               return render(request, 'core/addproduct.html', {'form': fm}) 
        else:
            fm = EditProductForm()
            return render(request, 'core/addproduct.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login')


def delete_product(request,id):
    if request.user.is_authenticated:
        fm = Product.objects.get(pk=id)
        fm.delete()
        messages.success(request,'Product Deleted Successfully...')
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')

