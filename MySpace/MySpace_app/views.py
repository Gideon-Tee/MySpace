from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='signin')
def index(request):
    return render(request, 'my_space/index.html')

@login_required(login_url='signin')
def settings(request):
    userProfile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('profileImg') == None:
            image = userProfile.profileImage
        else:
            image = request.FILES.get('profileImg')
        
        bio = request.POST['bio']
        location = request.POST['location']

        userProfile.profileImage = image
        userProfile.bio = bio
        userProfile.location = location
        userProfile.save()

        return redirect('settings')

    context = {
        'userProfile': userProfile
    }

    return render(request, 'my_space/setting.html', context)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already taken')
                return redirect('signup')
            else:
                new_user = User.objects.create_user(username=username, password=password)
                new_user.save()
                #log user in
                userLogin = auth.authenticate(username=username, password=password)
                auth.login(request, userLogin)

                #Create profile object for the user
                userModel = User.objects.get(username=username)
                userProfile = Profile.objects.create(user=userModel, id_user=userModel.id)
                userProfile.save()
                return redirect('settings')
        else:
            messages.error(request, 'passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'my_space/signup.html')
    

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
            return redirect('signin')
        
    else:
        return render(request, 'my_space/signin.html')
    
@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')