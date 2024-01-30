from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Add_Product
import os
from .models import Ordered_Product
from dotenv import load_dotenv
from rest_framework import status



def configure():
    load_dotenv()

    

# @login_required(login_url='signin')
def base(request):
    configure()
    return render(request, 'base.html')


# @login_required(login_url='signin')
def dashboard(request):
    configure()
    return render(request, 'admin_app/dashboard.html')



# @login_required(login_url='signin')
def diet_plan(request):
    configure()
    return render(request, 'admin_app/diet_plan.html')


# @login_required(login_url='signin')
def order_list(request):
    configure()
    return render(request, 'admin_app/order_list.html')



from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# @login_required(login_url='signin')
def add_product(request):
    configure()
    message = ''
    if request.method == "POST":         
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        additionalField1 = request.POST.get('additionalField1')
        additionalField2 = request.POST.get('additionalField2')
        additionalField3 = request.POST.get('additionalField3')
        additionalField4 = request.POST.get('additionalField4')
        additionalField5 = request.POST.get('additionalField5')
        print(product_name,description,price,quantity,additionalField1,additionalField2,additionalField3,additionalField4,additionalField5)

        create_product = Add_Product(
            product_name=product_name,
            description=description,
            price=price,
            quantity=quantity,
            additionalField1=additionalField1,
            additionalField2=additionalField2,
            additionalField3=additionalField3,
            additionalField4=additionalField4,
            additionalField5=additionalField5
        )
        create_product.save()
        message = 'Product Added Successfully. Check the Product List Page'
        # Redirect to the product list page after successful submission
        # return redirect('/product_list', {'message': message})

    return render(request, 'admin_app/add_product.html', {'message': message})




# @login_required(login_url='signin')
def product_list(request):
    configure()
    products = Add_Product.objects.all()
    return render(request, 'admin_app/product_list.html', {'products': products})




# @login_required(login_url='signin')
# def add_profile(request):
#     message = ''
#     if request.method == "POST":
#         user_name = request.POST.get('user_name')
#         age = request.POST.get('age')
#         height = request.POST.get('height')
#         weight = request.POST.get('weight')
#         any_disease = request.POST.get('any_disease', '')
#         allergies = request.POST.get('allergies', '')

#         create_profile = UserProfile(
#             user_name=user_name,
#             age=age,
#             height=height,
#             weight=weight,
#             any_disease=any_disease,
#             allergies=allergies
#         )
#         create_profile.save()
#         message = 'Profile Added Successfully.'

#     return render(request, 'admin_app/add_profile.html', {'message': message})




# @login_required(login_url='signin')
# def profile_list(request):
#     profiles = UserProfile.objects.all()
#     return render(request, 'admin_app/profile_list.html', {'profiles': profiles})



# @login_required(login_url='signin')
def reward_list(request):
    configure()
    return render(request, 'admin_app/reward_list.html')


# @login_required(login_url='signin')
def subscription_plan(request):
    configure()
    return render(request, 'admin_app/subscription_plan.html')


# @login_required(login_url='signin')
def user_list(request):
    configure()
    return render(request, 'admin_app/user_list.html')


# @login_required(login_url='signin')
def wallet_management(request):
    configure()
    return render(request, 'admin_app/wallet_management.html')


# @login_required(login_url='signin')
def order_list(request):
    configure()
    return render(request, 'admin_app/order_list.html')


# @login_required(login_url='signin')
def add_product(request):
    configure()
    return render(request, 'admin_app/add_product.html')


# @login_required(login_url='signin')
def product_list(request):
    configure()
    return render(request, 'admin_app/product_list.html')


# @login_required(login_url='signin')
def profile_list(request):
    configure()
    return render(request, 'admin_app/profile_list.html')


# @login_required(login_url='signin')
def add_profile(request):
    configure()
    return render(request, 'admin_app/add_profile.html')


# @login_required(login_url='signin')
def reward_list(request):
    configure()
    return render(request, 'admin_app/reward_list.html')


# @login_required(login_url='signin')
def subscription_plan(request):
    configure()
    return render(request, 'admin_app/subscription_plan.html')


# @login_required(login_url='signin')
def user_list(request):
    configure()
    return render(request, 'admin_app/user_list.html')


# @login_required(login_url='signin')
def wallet_management(request):
    configure()
    return render(request, 'admin_app/wallet_management.html')


# @login_required(login_url='signin')
def transaction_history(request):
    configure()
    return render(request, 'admin_app/transaction_history.html')




def signup(request):
    configure()
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':

        first_name = request.POST.get('First_Name')
        last_name = request.POST.get('Last_Name')
        email = request.POST.get('Email')
        mobile_number = request.POST.get('Mobile_Number')
        password = request.POST.get('Password')
        confirm_password = request.POST.get('Confirm_Password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('/signup/')
        
        # Create a new user
        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        login(request, user)
        messages.success(request, 'Account created successfully')
        return redirect('/signin/') 
    
    return render(request, 'signup.html')



def signin(request):
    configure()
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/') 
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'signin.html')


# @login_required(login_url='signin')
def logout(request):
    configure()
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/signin/')





# API VIEWS.PY

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response



from .serializers import Add_ProductSerializer
@api_view(['GET'])
def product_list_api(request):
    configure()
    products = Add_Product.objects.all()
    product_serializer = Add_ProductSerializer(products, many=True)

    return Response({'status': 200, 'payload': product_serializer.data})


@api_view(['POST'])
def add_product_api(request):
    configure()
    if request.method == 'POST':
        serializer3 = Add_ProductSerializer(data=request.data)
        if serializer3.is_valid():
            serializer3.save()
            return Response({'status': 201, 'message': 'Product added successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 400, 'message': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
    


# from .serializers import UserProfileSerializer
# @api_view(['GET'])
# def user_list_api(request):
#     users = User.objects.all()
#     users_serializer = UserSerializer(users, many=True)

#     return Response({'status': 200, 'payload': users_serializer.data})


# @api_view(['POST'])
# def add_user_api(request):
#     if request.method == 'POST':
#         serializer4 = UserSerializer(data=request.data)
#         if serializer4.is_valid():
#             # Create a new user with secure password handling
#             user1 = serializer4.save()
#             user1.set_password(request.data['password'])
#             user1.save()

#             return Response({'status': 201, 'message': 'User added successfully'}, status=status.HTTP_201_CREATED)
#         return Response({'status': 400, 'message': 'Invalid data provided', 'errors': serializer4.errors}, status=status.HTTP_400_BAD_REQUEST)
    






from .serializers import Ordered_ProductSerializer
@api_view(['GET'])
def order_list_api(request):
    configure()
    orders = Ordered_Product.objects.all()
    orders_serializer = Ordered_ProductSerializer(orders, many=True)

    return Response({'status': 200, 'payload': orders_serializer.data})


@api_view(['POST'])
def add_order_api(request):
    configure()
    if request.method == 'POST':
        serializer1 = Ordered_ProductSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response({'status': 201, 'message': 'Order added successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 400, 'message': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)


# from .serializers import wallet_Serializer
# @api_view(['GET'])
# def wallet_list_api(request):
#     wallets = Wallet.objects.all()
#     wallets_serializer = wallet_Serializer(wallets, many=True)

#     return Response({'status': 200, 'payload': wallets_serializer.data})





# @api_view(['POST'])
# def add_money_to_wallet(request):
#     if request.method == 'POST':
#         print(request.data)
#         serializer = wallet_Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'status': 201, 'message': 'Money added to wallet successfully'}, status=status.HTTP_201_CREATED)
#         return Response({'status': 400, 'message': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)











































# def signin(request):
#     if request.method=="POST":
#         Email=request.POST['Email']
#         Password=request.POST['Password']
        
#         user = authenticate(email=Email, password=Password)
#         if user is not None:
#             login(request, user)
#             return redirect('/')
#         else:
#             messages.error(request, "Invalid Credentials !!")
#             return redirect('/signin/')        
        
#     return render(request, 'signin.html')





# def signup(request):
#     if request.method=="POST":
#         First_Name=request.POST['First_Name']
#         Last_Name=request.POST['Last_Name']
#         Email=request.POST['Email']
#         Mobile_Number=request.POST['Mobile_Number']
#         Password=request.POST['Password']        
#         Confirm_Password=request.POST['Confirm_Password']
#         if len(Mobile_Number) != 10:
#             messages.error(request,'Number should be of 10 digit')
#             return redirect('/signup/')
#         elif Password!=Confirm_Password:
#             messages.error(request,'password and confirm password should be same')
#             return redirect('/signup/')
#         else:
#             user=User.objects.create(username=Email,password=Confirm_Password,email=Email)
#             user.first_name=First_Name
#             user.last_name=Last_Name
#             user.save()
#             messages.success(request, "Your Account is Successfully Created. Please Login !!")            
#             return redirect('/signin/')
        
#     return render(request, 'signup.html')