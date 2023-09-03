from django.db import models

from django.contrib.auth.models import User


# Create your models here.




class UserDetails(models.Model):

     blogger = models.OneToOneField(User,on_delete=models.CASCADE , name="user_extra_info")

     mobile_number = models.BigIntegerField(default=123456789)

     gender = models.CharField(choices=(('M','Male'),('F','Female'),('C','Custom')),default='C',max_length=1)

     date_of_birth = models.DateField()
     
     is_blogger= models.BooleanField(default=False)
     

     def __str__(self):

          return f'{self.user_extra_info.first_name} {self.user_extra_info.last_name} {self.mobile_number}'
     
     

class BlogInfo(models.Model):

     title = models.CharField(max_length=255,default='Unknown')
     
     img = models.ImageField(upload_to='media/blog_imgs',null=True,blank=True)
     
     desc = models.TextField(default='data not added')
     author = models.ForeignKey(User,on_delete=models.CASCADE, name='blogger')
     
     created_at = models.DateTimeField(auto_now=True)
     
     def __str__(self):
          return self.title
     