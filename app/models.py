from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.conf import settings

class Professor(models.Model):
	nome = models.CharField('Nome', max_length=100, unique = True)
	
	def __str__(self):
		return self.nome

	class Meta:
		verbose_name='Professor';
		verbose_name_plural='Professores'

class Bolsista(models.Model):
	
	TIPO_CHOICES = (
	    (0, 'Voluntário'),
	    (1, 'Remunerado'),
	)


	nome = models.CharField('Nome', max_length=100)
	cartao_rfid = models.CharField('Cartão RFID', max_length=100, null=True)
	professor = models.ForeignKey(Professor, verbose_name='Professor', related_name='bolsista_professor', on_delete=models.CASCADE, default=True)
	tipo_bolsa = models.IntegerField('Tipo', choices=TIPO_CHOICES)
	carga_horaria_semanal = models.IntegerField('Carga Horaria (semanal)', validators=[MinValueValidator(1)])
	
    
	def __str__(self):
		return self.nome


	class Meta:
		verbose_name='Bolsista'
		verbose_name_plural='Bolsistas'

class Acesso(models.Model):
	bolsista = models.ForeignKey(Bolsista, verbose_name='Bolsista', related_name='bolsista_acesso', on_delete=models.CASCADE)
	hora_entrada = models.TimeField('Entrada', null=True, blank=True)
	hora_saida = models.TimeField('Saída', null = True, blank=True)
	total_horas = models.TimeField('Total', null = True, blank = True)


	class Meta:
	 	verbose_name = 'Acesso'
	 	verbose_name_plural = 'Acessos'

