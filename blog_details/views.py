from django.shortcuts import render
from django.http import request,HttpResponse
from django.contrib.auth.models import User
from . models import *

# Create your views here.

def home(request):
     return HttpResponse("welcome to blogging site")
     
     
     
def signup(request):
          
     if request.method == "POST":
          print(request.POST)
          
          first_name = request.POST['first_name']
          last_name = request.POST['last_name']
          username= request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          
          user_info = User.objects.create(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
          
          mobile_number = request.POST['mobile_number']
          gender = request.POST['gender']
          date_of_birth = request.POST['date_of_birth']
          
          if request.POST['user_type'] == "True":
               is_blogger = True
          else:
               is_blogger = False
               
          try:
               UserDetails.objects.create(user_extra_info_id= user_info.id,mobile_number=mobile_number,gender=gender,date_of_birth=date_of_birth,is_blogger=is_blogger )
               return HttpResponse('Your account has been Created')
          except:
               return HttpResponse('sorry something wents wrong')
          
     return render(request,'account/signup.html')