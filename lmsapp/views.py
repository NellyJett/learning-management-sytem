from django.shortcuts import render, redirect
from lmsapp.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import ast  # for safer evaluation
import matplotlib.pyplot as plt
from lmsapp.models import (
    Profile,
    Grade,
    User,
)

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registeration.html', {'form': form})
        
@login_required
def result(request):
    prof = Profile.objects.filter(user = User.objects.get(username=self.request.user)).first()
    curr = Grade.objects.filter(user=prof).first()

    l = eval(curr.ut1)
    plt.clf()
    data = {'IP':l[0], 'MRF':l[1], 'FOC':l[2], 'RA':l[3], 'SAT':l[4]}
    courses = list(data.keys())
        