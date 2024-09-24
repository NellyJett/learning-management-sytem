from django.shortcuts import render

def home(request):
    return render(request, 'home.html')






def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.clean_data.get('username')
            message = success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            form = UserRegistrationForm()
            return render(request, 'users/register.html', {'form':form})
        