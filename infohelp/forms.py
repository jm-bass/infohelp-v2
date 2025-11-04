from django import forms
from .models import Curso, Categoria, Dificuldade

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao']

class DificuldadeForm(forms.ModelForm):
    class Meta:
        model = Dificuldade
        fields = ['nome', 'descricao']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'titulo',
            'descricao',
            'categoria',
            'dificuldade',
            'imagem',
            'link_video',
            'carga_horaria',
            'ativo'
        ]
