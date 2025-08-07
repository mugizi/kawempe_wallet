from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ProfileForm
from .models import Profile

# Create your views here.
def register(request):  
    if request.method == 'POST':  
        form = UserProfileForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            return redirect('login')  
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