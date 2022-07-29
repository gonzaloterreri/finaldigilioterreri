from email.headerregistry import ContentDispositionHeader
from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.template.loader import render_to_string



from django.core.mail import send_mail



# Create your views here.

def contacto(request):
    formulario_contacto=FormularioContacto()
    
    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
           


            try:
                asunto=email
                mensaje=contenido
                mensaje_texto="texto"
                from_email="cosmefulanitoweb499@hotmail.com"
                to="cosmefulanitoweb499@hotmail.com"
                send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)
                
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")


    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
