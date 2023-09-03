from django.shortcuts import render,redirect
from django.http import request,HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from . models import *
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login")
def home(request):
     
     user = request.user
     user_info = UserDetails.objects.get(user_extra_info_id=user.id )

     all_blogs = BlogInfo.objects.all()
     
     return render(request,'blogging/home.html',{'all_blogs':all_blogs,"user_info":user_info})
     
     
     
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



def login(request):
     
     if request.method == "POST":
          
          username = request.POST['username']
          password = request.POST['password']
          
          user = authenticate(username=username,password=password)

          
          if user is not None:

               if user.is_active:
                    auth.login(request,user)
                    return redirect('homepage')
               else:
                    return HttpResponse('user is not active')
          else:
               return HttpResponse("please enter the correct details")
          
     
     return render(request,'account/login.html')


@login_required(login_url="/login")
def blog_info(request,id):
     
     try:
          blog = BlogInfo.objects.get(id=id)
          return render(request,'blogging/blog_info.html',{"blog":blog})
     
     except:
          return HttpResponse("Page not found")
     
@login_required(login_url="/login")
def my_blogs(request):
     
     user = request.user
     
     blogs = BlogInfo.objects.filter(blogger_id = user.id)
     
     return render(request,"account/my_blogs.html",{"blogs":blogs})

@login_required(login_url="/login")
def new_blog(request):
     
     
     if request.method == "POST":
          
          title  = request.POST["title"]
          desc = request.POST['desc']
          img = request.FILES['img']
          
          user = request.user
          try:
               BlogInfo.objects.create(title=title,desc=desc,img=img,blogger_id=user.id)
               return redirect('my_blogs')
          except:
               return HttpResponse("something went wrong")
          
     
     return render(request,'account/new_blog.html')


@login_required(login_url="/login")
def delete_blog(request,id):
     
     try:
          blog = BlogInfo.objects.get(id=id)
          user = request.user        
          
          if blog.blogger.id == user.id:
               blog.delete()
               return redirect('my_blogs')
          else:
               return HttpResponse("something went wrong")
          
     except:
          return HttpResponse("something went wrong")
     


@login_required(login_url="/login")
def edit_blog(request,id):
     
     
     if request.method == "POST":
          
          try:
               blog = BlogInfo.objects.get(id =id)
               user = request.user
               
               if blog.blogger.id == user.id:
                    title   = request.POST["title"]
                    desc   = request.POST["desc"]
                    img   = request.FILES["img"]
                    
                    blog.title = title
                    blog.desc = desc
                    blog.img = img
                    blog.save()
                    return redirect('my_blogs')
               else:
                    return HttpResponse("something went wrong")
          except:
               return HttpResponse("something went wrong")
     
     
     
     try:
          blog = BlogInfo.objects.get(id=id)
          
          user = request.user
          
          if blog.blogger.id == user.id:
               return render(request,'account/edit_blog.html',{'blog':blog})
          else:
               return HttpResponse("something went wrong")
          
     except:
          return HttpResponse("something went wrong")
     

@login_required(login_url="/login")
def logout(request):
     try:
          auth.logout(request)
          return redirect('login')
     except:
          return redirect('login')
