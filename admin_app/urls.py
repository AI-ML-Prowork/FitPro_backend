from django.contrib import admin
from django.urls import path
from . views import *
from rest_framework.routers import DefaultRouter
from . views import product_list_api


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('logout/', logout, name='logout'),


    path("", base, name="base"),
    path("dashboard", dashboard, name='dashboard'),
    path("diet_plan", diet_plan, name='diet_plan'),
    path("order_list", order_list, name='order_list'),

    path("add_product", add_product, name='add_product'),
    path("product_list", product_list, name='product_list'),

    path("profile_list", profile_list, name='profile_list'),
    path("add_profile", add_profile, name='add_profile'),

    path("reward_list", reward_list, name='reward_list'),
    path("subscription_plan", subscription_plan, name='subscription_plan'),
    path("user_list", user_list, name='user_list'),
    path("wallet_management", wallet_management, name='wallet_management'),
    path("transaction_history", transaction_history, name='transaction_history'),



    #API CALLS 
    path("product_list_api", product_list_api, name='product_list_api'),
    path("add_product_api", add_product_api, name='add_product_api'),

    path("user_list_api", user_list_api, name='user_list_api'),
    path("add_user_api", add_user_api, name='add_user_api'),

    path("profile_list_api", profile_list_api, name='profile_list_api'),
    path("add_profile_api", add_profile_api, name='add_profile_api'),

    path("order_list_api", order_list_api, name='order_list_api'),
    path("add_order_api", add_order_api, name='add_order_api'),

    path("wallet_list_api", wallet_list_api, name='wallet_list_api'),
    path("add_money_to_wallet", add_money_to_wallet, name='add_money_to_wallet'),




    
]