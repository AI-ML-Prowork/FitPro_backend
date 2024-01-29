from django.urls import path
from . views import *

urlpatterns = [
    # path("add_user_api", add_user_api, name='add_user_api'),

    path("add_profile_api", add_profile_api, name='add_profile_api'),

    # path("wallet_list_api", wallet_list_api, name='wallet_list_api'),
    path("add_money_to_wallet", add_money_to_wallet, name='add_money_to_wallet'),
    
]
