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
        return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer2.errors}, status=status.HTTP_400_BAD_REQUEST)
    


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
        return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




from .serializers import UserProfileSerializer
@api_view(['GET'])
def user_list_api(request):
    users = User.objects.all()
    users_serializer = UserSerializer(users, many=True)

    return Response({'status': 200, 'payload': users_serializer.data})


@api_view(['POST'])
def add_user_api(request):
    if request.method == 'POST':
        serializer4 = UserSerializer(data=request.data)
        if serializer4.is_valid():
            # Create a new user with secure password handling
            user1 = serializer4.save()
            user1.set_password(request.data['password'])
            user1.save()

            return Response({'status': 201, 'message': 'User added successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 400, 'message': 'Invalid data provided', 'errors': serializer4.errors}, status=status.HTTP_400_BAD_REQUEST)
    

from .serializers import Add_reward_Serializer
from .models import Add_reward
class rewards_api(APIView):

    def get(self, request):
        configure()
        rewards = Add_reward.objects.all()
        rewards_serializer = Add_reward_Serializer(rewards, many=True)
        return Response({'status': 200, 'payload': rewards_serializer.data})
    
    def post(self, request):
        configure()
        if request.method == 'POST':
            print(request.data)
            serializer5 = Add_reward_Serializer(data=request.data)
            if serializer5.is_valid():
                serializer5.save()
                return Response({'status': 201, 'message': 'Reward added successfully'}, status=status.HTTP_201_CREATED)
            return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer5.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk):
        configure()
        rewards = Add_reward.objects.get(pk=pk)
        serializer5 = Add_reward_Serializer(rewards, data=request.data)
        if serializer5.is_valid():
            serializer5.save()
            return Response({'status': 200, 'message': 'Reward updated successfully'}, status=status.HTTP_200_OK)
        return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer5.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        configure()
        rewards = Add_reward.objects.get(pk=pk)
        rewards.delete()
        return Response({'status': 200, 'message': 'Reward deleted successfully'}, status=status.HTTP_200_OK)
    


from .serializers import Add_Order_Serializer
from .models import Add_Order


class orders_api(APIView):

    def get(self, request):
        configure()
        orders = Add_Order.objects.all()
        orders_serializer = Add_Order_Serializer(orders, many=True)
        return Response({'status': 200, 'payload': orders_serializer.data})
    
    def post(self, request):
        configure()
        if request.method == 'POST':
            print(request.data)
            serializer6 = Add_Order_Serializer(data=request.data)
            if serializer6.is_valid():
                serializer6.save()
                return Response({'status': 201, 'message': 'Order added successfully'}, status=status.HTTP_201_CREATED)
            return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer6.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk):
        configure()
        orders = Add_Order.objects.get(pk=pk)
        serializer6 = Add_Order_Serializer(orders, data=request.data)
        if serializer6.is_valid():
            serializer6.save()
            return Response({'status': 200, 'message': 'Order updated successfully'}, status=status.HTTP_200_OK)
        return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer6.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        configure()
        orders = Add_Order.objects.get(pk=pk)
        orders.delete()
        return Response({'status': 200, 'message': 'Order deleted successfully'}, status=status.HTTP_200_OK)
    


    
    