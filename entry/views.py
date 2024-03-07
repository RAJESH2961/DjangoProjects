from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been successfully logged in !")
            # Redirect to a success page.
            return redirect('home')  # Redirect to the home page after login.
        else:
            messages.success(request,"There was an error while Logging in")
            # Return an 'invalid login' error message.
            #return render(request, 'login.html', {'error_message': 'Invalid login credentials.'})
    else:
        # Render the login form.
        #return render(request, 'login.html')
        return render(request, 'home.html')


    

def user_logout(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')  # Redirect to the home page after logout.
