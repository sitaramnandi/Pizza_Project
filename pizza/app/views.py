from django.shortcuts import render,redirect
from app.models import *
# from locust import User
from django.contrib import messages
from django.contrib.auth.models import User# Create your views here.
from django.contrib.auth import login,authenticate
from instamojo_wrapper import Instamojo
from django.conf import settings
api = Instamojo(api_key=settings.API_KEY,
                auth_token=settings.AUTH_TOKEN,endpoint="https://test.instamojo.com/api/1.1/")



def index(request):
    pizza_list=Pizza.objects.all()
    context={"pizza_list":pizza_list}

    return render(request,"app/index.html",context)


def register_page(request):
    if request.method=="POST":

        try:
            username=request.POST.get("username")
            password=request.POST.get("password")
            user_obj=User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "UserName Allresdu zexist")
                return redirect("/register/")
            user_obj=User.objects.get_or_create(username=username,password=password)
            print(user_obj.password)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account Creted")
            return redirect("/login")
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect("/register")

    return render(request,"app/register.html")

def login_page(request):
    if request.method=="POST":

        try:
            username=request.POST.get("username")
            password=request.POST.get("password")
            user_obj=User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "UserName not found")
                return redirect("/login/")
            user_obj=authenticate(username=username,password=password)
            if user_obj:
                login(request,user_obj)
                return redirect("/")
            messages.success(request, "wrong password")
            return redirect("/login")
        except Exception as e:
            messages.error(request, "Something went wrong")
    return render(request,"app/login.html")


def add_cart(request,pizza_uid):
    user=request.user
    pizza_obj=Pizza.objects.get(uid=pizza_uid)
    cart,_=Cart.objects.get_or_create(user=user,is_paid=False)
    cart_items=CartItems.objects.create(
        cart=cart,
        pizaa=pizza_obj
    )
    return redirect("/")
    # return render(request,"app/add_cart.html")


def cart(request):
    carts=Cart.objects.get(is_paid=False,user=request.user)
    
    response=api.payment_request_create(
        amount= carts.get_cart_total(),
        purpose="Order",
        buyer_name=request.user.username,
        email="studytapdevloper@gmail.com",
        redirect_url="http://127.0.0.1:8000/success/"

    )
    carts.instamojo_id=response["payment_request"]["id"]
    carts.save()
    context={"carts":carts,"payment_url":response["payment_request"]["longurl"]}
    print(response)
    return render(request,"app/cart.html",context)

def remove_cart_items(request,cart_item_uid):
    try:
        CartItems.objects.get(uid=cart_item_uid).delete()
        return redirect("/cart")
    except Exception as e:
        print(e)


def orders(request):
    orders=Cart.objects.filter(is_paid=True,user=request.user)
    context={"orders":orders}
    return render(request,"app/oder.html",context)


def success(request):
    payment_request=request.GET.get("payment_request_id")
    cart=Cart.objects.get(instamojo_id=payment_request)
    cart.is_paid=True
    cart.save()
    return redirect("/orders")


