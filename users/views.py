from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ProfileForm
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
def register(request):  
    if request.method == 'POST':  
        form = UserProfileForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            return redirect('account_list')  
    else:  
        form = UserProfileForm()  
    return render(request, 'registration/register.html', {'form': form})  

@login_required  
def edit_profile(request):  
    profile, created = Profile.objects.get_or_create(user=request.user)  
    if request.method == 'POST':  
        form = ProfileForm(request.POST, request.FILES, instance=profile)  
        if form.is_valid():  
            form.save()  
            return redirect('profile_detail')  
    else:  
        form = ProfileForm(instance=profile)  
    return render(request, 'profiles/profile_form.html', {'form': form})  

@login_required  
def profile_detail(request):  
    profile = Profile.objects.get(user=request.user)  
    return render(request, 'profiles/profile_detail.html', {'profile': profile})


@login_required
def account_list(request):
    qs = User.objects.select_related('profile').all()
    return render(request, 'profiles/user_list.html', {'users': qs})

def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        error = 'Invalid credentials'
    return render(request, 'login.html', {'error': error})