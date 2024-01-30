from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
# from .models import Add_Product
# from .models import UserProfile
# from .models import Ordered_Product
# from .models import Wallet
from rest_framework import status
from .models import UserProfile
from .models import Wallet
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()








# API VIEWS.PY

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import UserProfileSerializer
from .serializers import UserSerializer
@api_view(['GET'])
def profile_list_api(request):
    configure()
    profiles = UserProfile.objects.all()
    profiles_serializer = UserProfileSerializer(profiles, many=True)

    return Response({'status': 200, 'payload': profiles_serializer.data})



@api_view(['POST'])
def add_profile_api(request):
    configure()
    if request.method == 'POST':
        serializer2 = UserProfileSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response({'status': 201, 'message': 'Profile added successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 400, 'message': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
    


from .serializers import wallet_Serializer
@api_view(['GET'])
def wallet_list_api(request):
    configure()
    wallets = Wallet.objects.all()
    wallets_serializer = wallet_Serializer(wallets, many=True)

    return Response({'status': 200, 'payload': wallets_serializer.data})





@api_view(['POST'])
def add_money_to_wallet(request):
    configure()
    if request.method == 'POST':
        print(request.data)
        serializer = wallet_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'message': 'Money added to wallet successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 400, 'message': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
