from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create user
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        # Optionally, you can do additional actions like login the user after creation
        # For example:
        # login(request, user)

        return render(request, 'signup.html', {'message': 'User created successfully'})
    else:
        return render(request, 'signup.html')

def LoginPage(request):
    return render(request, 'login.html')
