from django.contrib import admin
from .models import Bolsista, Professor, Acesso


class BolsistaAdmin(admin.ModelAdmin):

    list_display = ['nome']
    search_fields = ['name']


class AcessoAdmin(admin.ModelAdmin):
	list_display = ['bolsista', 'hora_entrada', 'hora_saida','total_horas']



class ProfessorAdmin(admin.ModelAdmin):

    list_display = ['nome']
    search_fields = ['name']


admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Bolsista, BolsistaAdmin)
admin.site.register(Acesso, AcessoAdmin)