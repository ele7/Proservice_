from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, 'index.html')

def contact(request):
    success = False
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Aquí podrías guardar en DB o enviar email
        send_mail(
            f'Mensaje de {first_name} {last_name}',
            message,
            email,  # desde
            ['info@tusitio.com'],  # a quién enviar
        )
        success = True

    return render(request, 'contacto/contact.html', {'success': success})

def home(request):
    return render(request, 'home/home.html')

def portafolio(request):
    return render(request, 'proyectos/portafolio.html')