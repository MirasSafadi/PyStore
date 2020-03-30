from django.shortcuts import render
from PyStoreApp.signin_form import LoginForm
from .models import Product
from .models import User
from django.shortcuts import redirect
# Create your views here.


def home(request, user=None):
    user1 = User(0,"koko","koko@koko.vom","1111","052250")
    if user:
        return render(request, "home.html",{'user':user,'isLoggedIn': True})
    else:
        return render(request, "home.html",{'user':user1,'isLoggedIn': False})



def signin(request):
 if request.method == 'POST':
        # Get the posted form
      MyLoginForm = LoginForm(request.POST)
      if MyLoginForm.is_valid():
        mail = MyLoginForm.cleaned_data['mail']
        password = MyLoginForm.cleaned_data['password']

        # mail = MyLoginForm.cleaned_data['email']
        # your code using database
         # if user.mail == 'Fouad.bisharat@gmail.com' and user.pass == '1234' --> if user.mail and user.pass in database and coreect
         #objects.filter(slug_url=slug).exists()
        if User.objects.filter(email=mail).exists():
            user = User.objects.get(email=mail)
            if user.password == password:
                return render(request, 'home.html', {"user": user})

            else:
                return render(request, 'signin.html', {"mail": mail, "password": password})

        # if mail == 'Fouad.bisharat@gmail.com'or mail == 'dana@gmail.com':
        #     # return redirect('welcome') # just to request first time the page
        #     return render(request, 'base_user.html', {"mail": mail})
        else:
            return render(request, 'signin.html', {"mail": mail, "password": password})
      else:
        return render(request, 'signin.html', {"mail": "bad user name", "password": "bad password"})
 else:
   return render(request, 'signin.html', {"mail" : "nomail","password":"nopassword" })    

   
def signout(request):
    return render(request,"signout.html")

def register(request):
    return render(request,"register.html")

def cart(request):
    return render(request,"cart.html")

def userAccount(request):
    return render(request,"userAccount.html")

def category(request):
    #?how to privew the mail always?
    return render(request,"category.html",)

def all_products(request):
    all_products=Product.objects.all
    return render(request,"all_products.html",{'all_products':all_products})

def product(request, id):
    # After connecting to DB, the data of product dictionary will be changed accordingly
    product=Product.objects.get(pk=id)
    # product={'id': 123456789, 'description' : 'hello', 'price':35}
    return render(request,"product.html",{'product':product})