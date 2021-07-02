from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from users.models import Profile
from django.db.utils import IntegrityError

@login_required
def update_profile(request):
    return render(request, 'users/update_profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})

    return render(request, 'users/login.html')

def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST.get('passwd', True)
        passwd_confirmation = request.POST.get('passwd_confirmation', True)




        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        user.profile.profile_picture = request.POST.get('profile_picture')
        user.profile.profile_biography = request.POST.get('profile_biography')
        user.profile.save()

        user.profile = Profile
        user.save()
        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')