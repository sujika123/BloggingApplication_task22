from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from blogapp.forms import LoginForm, userloginform, bloggingform
from blogapp.models import blog


# Create your views here.
def home(request):
    return render(request,'home.html')


def register(request):
    form = LoginForm()
    form1 = userloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = userloginform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            usr = form1.save(commit=False)
            usr.user = user
            usr.save()
            return redirect("loginview")
    return render(request,'registration.html',{'form':form,'form1':form1})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('adminhome')
        if user is not None and user.is_user:
            login(request,user)
            return redirect('userhome')
        else:
            messages.info(request,'Invalid credentials')
    return render(request,'login.html')

def adminhome(request):
    return render(request,'adminhome.html')

def userhome(request):
    return render(request,'userhome.html')

def add_blog(request):
    form = bloggingform()
    u = request.user
    if request.method == 'POST':
        form = bloggingform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('view_blog')
    return render(request,'add_blog.html',{'form':form})



def view_blog(request):
    u = request.user
    data = blog.objects.all()
    return render(request, 'view_blog.html', {'data': data})

def view_selfBlog(request):
    u = request.user
    data = blog.objects.filter(user=u)
    return render(request, 'view_update_selfBlog.html', {'data': data})


def delete_blog(request,id):
    b = blog.objects.get(id=id)
    b.delete()
    return redirect('view_selfBlog')


def update_blog(request,id):
    user = blog.objects.get(id=id)
    form = bloggingform(instance=user)
    if request.method == "POST":
        form= bloggingform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('view_selfBlog')
    return render(request,'update_blog.html',{'form':form})

