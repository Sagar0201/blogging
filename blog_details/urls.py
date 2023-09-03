from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('',views.home,name="homepage"),
     path('signup/',views.signup , name='signup'),
     path('login/',views.login, name='login'),
     
     path('<int:id>',views.blog_info, name="blog_info"),
     path('my-blogs',views.my_blogs,name="my_blogs"),
     path('new-blog',views.new_blog,name="new_blog"),
     path('delete-blog/<int:id>',views.delete_blog,name="delete_blog"),
     path('edit-blog/<int:id>',views.edit_blog,name="edit_blog"),
     path('logout',views.logout,name="logout"),
     
     
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)