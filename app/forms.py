from django import forms
from .models import Bolsista, Professor, Acesso

class ProfessorForm(forms.ModelForm):
	class Meta:
		model = Professor
		fields = ['nome']


class BolsistaForm(forms.ModelForm):
	class Meta:
		model = Bolsista
		fields = ['nome','professor','tipo_bolsa','carga_horaria_semanal']


class AcessoForm(forms.ModelForm):
	class Meta:
		model = Acesso
		fields = ['bolsista']