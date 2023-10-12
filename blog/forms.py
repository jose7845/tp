from django import forms

class FormComentario(forms.Form):
    autor=forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class" : "form-control" ,
            "placeholder" : "ingresa el nombre del autor"
        })
    )
    
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            "class" : "form-control" ,
            "placeholder" : "deja tu comentario aqui"
        })
    )