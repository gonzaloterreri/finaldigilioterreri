from django import forms
from django.shortcuts import redirect, render 
from blog.models import Post, Categoria
from .forms import PostFormulario

# Create your views here.

def blog(request):

    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria,"posts": posts})

def crear_post(request):
    if request.method == "POST":
        formulario = PostFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            
            post = Post(titulo=info["titulo"],contenido=info["contenido"],imagen=info["imagen"],autor=info["autor"])
            post.save()
            return redirect("Blog")
        return render(request,"blog/formulario_blog.html",{'form': formulario})
    
    
    formulario = PostFormulario()
    return render(request,"blog/formulario_blog.html",{'form': formulario})
    
     