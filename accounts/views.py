from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistoForm
from sesame.utils import get_token
from django.core.mail import send_mail
import sesame.utils 


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portfolio')
        else:
            return render(request, 'accounts/login.html', {'erro': 'Credenciais inválidas'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'accounts/logout.html')

def registo_view(request):
    if request.method == 'POST':
        form = RegistoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistoForm()
    return render(request, 'accounts/registo.html', {'form': form})

def magic_link_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = get_token(user)
            link = f'https://super-duper-guide-wrjwwrj64wjxf5rqx-8000.app.github.dev/accounts/magic/verificar/?sesame={token}'
            send_mail(
                'O teu link de acesso',
                f'Clica neste link para aceder: {link}',
                'noreply@portfolio.com',
                [email],
            )
            return render(request, 'accounts/magic_link_enviado.html')
        except User.DoesNotExist:
            return render(request, 'accounts/login.html', {'erro_magic': 'Email não encontrado'})
    return render(request, 'accounts/login.html')


def magic_link_login_view(request):
    from sesame.utils import get_user
    user = get_user(request)
    if user is not None:
        login(request, user, backend='sesame.backends.ModelBackend')
        return redirect('portfolio')
    return render(request, 'accounts/login.html', {'erro': 'Link inválido ou expirado'})
