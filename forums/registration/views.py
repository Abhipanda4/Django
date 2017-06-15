from django.shortcuts import render, redirect
from .forms import NewUserForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from  django.contrib.auth.forms import PasswordChangeForm
# from django.views.decorators.cache import cache_control

# Create your views here.
def index(request):
    return render(request, 'registration/index.html', {})

def signup(request):
    if request.user.is_authenticated():
        return redirect('registration:profiles')
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration:index')
    else:
        form = NewUserForm()
        context = {
            'form': form
        }
        return render(request, 'registration/signup.html', context)


@login_required(login_url='/registration/login/')
# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def profiles(request):
    context = {'user': request.user}
    return render(request, 'registration/profiles.html', context)

@login_required(login_url='/registration/login/')
def edit_profiles(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('registration:profiles')

    else:
        # getting the form  for first time
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
        return render(request, 'registration/edit_profiles.html', context)

@login_required(login_url='/registration/login/')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('registration:profiles')
        else:
            return redirect('registration:change_password')

    else:
        # getting the form  for first time
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'registration/edit_profiles.html', context)