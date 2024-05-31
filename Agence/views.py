from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Identifiants invalides. Veuillez réessayer."
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})
 
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Valider les données du formulaire
        if not first_name or not last_name or not email or not password or not confirm_password:
            error_message = "Tous les champs sont obligatoires."
            return render(request, 'register.html', {'error_message': error_message})
        if password != confirm_password:
            error_message = "Les mots de passe ne correspondent pas."
            return render(request, 'register.html', {'error_message': error_message})

        # Créer un nouvel utilisateur
        user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email, password=password)
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'register.html')