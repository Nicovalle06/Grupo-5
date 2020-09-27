from django import forms
from .models import Post, Comentario


class AltaPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['autor']

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('mensaje',)
        exclude = ['usuario']
