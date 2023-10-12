from django.shortcuts import render
from blog.models import Posteo , comentario
from blog.forms import FormComentario

def blog_index(request):
    posteos = Posteo.objects.all().order_by("-created_on")

    context={
        "posteos": posteos,
    
    }
    return render(request, "index.html", context)

def blog_detail(request, pk):
    posteo = Posteo.objects.get(pk=pk)
    
    formulario=FormComentario()
    if request.method == "POST":
        formulario = FormComentario(request.POST)
        
        if formulario.is_valid():
            Comentario = comentario(
                autor = formulario.cleaned_data["autor"],
                body = formulario.cleaned_data["body"],
                posteo = posteo
            )
            Comentario.save()
            
            formulario=FormComentario()
    comentarios = comentario.objects.filter(posteo=posteo)   
    
    context={
        "posteo" : posteo,
        "comentarios" : comentarios,
        "formulario" : formulario
    }
    
    return render(request, "detail.html" , context)
      
 