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
	model = Acesso
	fields = ['bolsista', 'data_entrada', 'data_saida', 'total_horas']