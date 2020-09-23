from django import forms
from .models import Post, Comentario


class AltaPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['autor']


class Comentarios(forms.Form):
    
    class Meta:
        model = Comentario
        fields = [
            'usuario',
            'mensaje',
            'fecha_publicación',            
        ]