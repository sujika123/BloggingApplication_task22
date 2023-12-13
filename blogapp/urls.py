from django.urls import path

from blogapp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register',views.register,name='register'),
    path('loginview',views.loginview,name='loginview'),
    path('userhome',views.userhome,name='userhome'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('add_blog',views.add_blog,name='add_blog'),
    path('view_blog',views.view_blog,name='view_blog'),
    path('view_selfBlog',views.view_selfBlog,name='view_selfBlog'),
    path('delete_blog/<int:id>/',views.delete_blog,name='delete_blog'),
    path('update_blog/<int:id>/',views.update_blog,name='update_blog'),

]