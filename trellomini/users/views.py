# users/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages

# Authentication Pages
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        messages.error(request, "Please correct the errors below.")
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})