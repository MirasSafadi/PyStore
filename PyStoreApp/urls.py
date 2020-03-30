from django.urls import path
from PyStoreApp import views

urlpatterns = [
  path('', views.home, name="home"),
  path('/<user>', views.home, name="home"),
  path('signin/', views.signin, name="signin"),
  path('signout/', views.signout, name="signout"),
  path('register/', views.register, name="register"),
  path('cart/', views.cart, name="cart"),
  path('userAccount/', views.userAccount, name="userAccount"),
  path('category/', views.category, name="category"),
  path('all_products/', views.all_products, name="all_products"),
  path('product/<id>', views.product, name="product"),
]
