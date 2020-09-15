from django import forms
from .models import Post


class AltaPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['autor', 'titulo', 'texto', 'fecha_publicacion']
