from django.shortcuts import redirect, render, HttpResponse
from .models import Post, Contact
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def home(request):
    post = Post.objects.all()
    last = post[len(post)-1]
    second_last = post[len(post)-2]
    third_last = post[len(post)-3]
    context = {
        'last': last,
        'second_last': second_last,
        'third_last':third_last,
    }
    return render(request, 'home/index.html', context)

def posts(request):
    post = Post.objects.all()
    context = {
        'post':post,
    }
    return render(request, 'home/posts.html', context)

def about(request):
    return HttpResponse("<h1>About Us</h1>")

def contact(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        purpose = request.POST["purpose"]

        if not User.objects.filter(username=username).exists():
            messages.warning(request, "User does not exists")
        
        if not User.objects.filter(email=email).exists():
            messages.warning(request, "Email does not exists")

        elif not User.objects.filter(email=email).exists() and not User.objects.filter(username=username).exists():
            messages.warning(request, "User does not exists")

        if User.objects.filter(email=email).exists() and User.objects.filter(username=username).exists():
            contacts = Contact(username=username, email=email, purpose=purpose)
            contacts.save()
            messages.success(request, "Contact Successfully Submited")


    return render(request, "home/contact.html")

def post_view(request, slug):
    post_view = Post.objects.filter(slug=slug).first()
    context = {
       'post_view':post_view, 
    }
    return render(request, "home/post_view.html", context)

def search(request):
    query = request.GET['query']
    title = Post.objects.filter(title__icontains=query)
    desc = Post.objects.filter(desc__icontains=query)
    posts = title.union(desc)
    context = {
        'posts': posts,
        'query':query,
    }
    return render(request, "home/search.html", context)

def signup(request):
    if request.method=="POST":
        f_name =request.POST["f_name"]
        l_name =request.POST["l_name"]
        userename1 =request.POST["username1"]
        email1 =request.POST["email1"]
        pass1 =request.POST["pass1"]
        pass2 =request.POST["pass2"]
        if pass1 == pass2:
            if User.objects.filter(username=userename1).exists() and User.objects.filter(email=email1).exists():
                messages.warning(request, "Username and Email are already taken")

            elif User.objects.filter(username=userename1).exists():
                messages.warning(request, "Username already taken")

            elif User.objects.filter(email=email1).exists():
                messages.warning(request, "Email already taken")
            else:
                user = User.objects.create_user(userename1, email1, pass1)
                user.first_name = f_name
                user.last_name = l_name
                user.save()
                messages.success(request, "User created :) !")


    return render(request, "home/signup.html")

def login(request):
    if request.method=="POST":
        userename_1 =request.POST["username_1"]
        pass_1 =request.POST["pass_1"]
        user = auth.authenticate(username=userename_1, password=pass_1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
            
        else:
            messages.warning(request, "Sign up First")

        

    return render(request, "home/login.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("/")
