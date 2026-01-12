from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.paginator import Paginator
from django.utils.html import strip_tags
import os
import time

from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def contact(request):
    success = False
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Simple rate-limiting: evitar envíos repetidos desde la misma sesión
            last = request.session.get('last_contact_ts', 0)
            now = time.time()
            if now - last < 10:  # 10 segundos de espera
                form.add_error(None, 'Por favor espera unos segundos antes de enviar de nuevo.')
            else:
                data = form.cleaned_data
                subject = f"Mensaje de {data.get('first_name')} {data.get('last_name', '')}".strip()
                # Desinfectar mensaje básico (remover tags HTML)
                message = strip_tags(data.get('message', ''))

                # Usar DEFAULT_FROM_EMAIL si está configurado; en desarrollo console backend está activo
                from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', 'webmaster@localhost')
                recipients = ['info@tusitio.com']

                email_msg = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=from_email,
                    to=recipients,
                    reply_to=[data.get('email')],
                )
                try:
                    email_msg.send(fail_silently=False)
                    request.session['last_contact_ts'] = now
                    success = True
                except Exception:
                    form.add_error(None, 'Error al enviar el mensaje. Intenta más tarde.')

    return render(request, 'contacto/contact.html', {'success': success, 'form': form})

def home(request):
    return render(request, 'home/home.html')

def portafolio(request):
    img_dir = os.path.join(settings.BASE_DIR, 'proservice', 'static', 'img')
    images = []
    try:
        for name in os.listdir(img_dir):
            if name.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
                images.append(name)
    except FileNotFoundError:
        images = []

    images.sort()
    # Construir URLs públicas para static (evita usar {% static %} con variables)
    image_urls = [settings.STATIC_URL.rstrip('/') + '/img/' + name for name in images]
    # Paginación: 15 por página (3 filas de 5 en escritorio)
    paginator = Paginator(image_urls, 15)
    page_number = request.GET.get('page') or 1
    page_obj = paginator.get_page(page_number)

    return render(request, 'proyectos/portafolio.html', {'page_obj': page_obj})