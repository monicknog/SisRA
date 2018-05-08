from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .forms import ProfessorForm, BolsistaForm, AcessoForm
from .models import Professor, Bolsista, Acesso
from datetime import datetime, time, date
import datetime
from django.utils import timezone

#Login e Home
def logar(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			login(request,form.get_user())
			return redirect('app:home')
		else:
			return render(request,"login.html",{"form":form})
	return render(request, "login.html", {"form":AuthenticationForm()})


@login_required(login_url='/login')
def home(request):
	if request.user.is_superuser:
		return render(request, 'home_admin.html')
	else:
		bolsistas = Bolsista.objects.all()
		return render(request, 'home_user_comum.html',{'bolsistas':bolsistas})

def home_professor(request):
	template_name = 'professor/home_professor.html'
	context = {}
	return render(request, template_name, context)

#Professor
@login_required(login_url='/login')
def create_professor(request):
	form = ProfessorForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('app:list_professor')
	
	return render(request, 'professor/cad_professor.html',{'form':form})


@login_required(login_url='/login')
def update_professor(request, pk):
	professor = Professor.objects.get(pk=pk)
	form = ProfessorForm(request.POST or None, instance = professor)

	if form.is_valid():
		form.save()
		return redirect('app:list_professor')
	return render(request,'professor/cad_professor.html',{'form':form})


@login_required(login_url='/login')
def list_professor(request):
	professores = Professor.objects.all()
	return render(request, 'professor/list_professor.html',{'professores':professores})


@login_required(login_url='/login')
def delete_professor(request, pk):
	try:
		professor = Professor.objects.get(pk=pk)
		if request.method == 'POST':
			professor.delete()
			return redirect('app:list_professor')
	except Professor.DoesNotExist:
		return redirect('app:home')
	return render(request,'professor/confirm_delete_professor.html',{'professor':professor})

#Bolsista
def home_bolsista(request):
	template_name = 'bolsista/home_bolsista.html'
	context = {}
	return render(request, template_name, context)


@login_required(login_url='/login')
def create_bolsista(request):
	form = BolsistaForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('app:list_bolsista')
	return render(request, 'bolsista/cad_bolsista.html', {'form':form})


@login_required(login_url='/login')
def update_bolsista(request, pk):
	bolsista = Bolsista.objects.get(pk=pk)
	form = BolsistaForm(request.POST or None, instance = bolsista)
	if form.is_valid():
		form.save()
		return redirect('app:list_bolsista')
	return render(request,'bolsista/cad_bolsista.html',{'form':form})


@login_required(login_url='/login')
def list_bolsista(request):
	bolsistas = Bolsista.objects.all()
	return render(request, 'bolsista/list_bolsista.html',{'bolsistas':bolsistas})


@login_required(login_url='/login')
def delete_bolsista(request, pk):
	try:
		bolsista = Bolsista.objects.get(pk=pk)
		if request.method == 'POST':
			bolsista.delete()
			return redirect('app:list_bolsista')
	except Bolsista.DoesNotExist:
		return redirect('app:home')
	return render(request,'bolsista/confirm_delete_bolsista.html',{'bolsista':bolsista})


#Acesso
@login_required(login_url='/login')
def create_ac(request):
	bolsistas = Bolsista.objects.all()
	return render(request, 'acesso/cad_acesso.html',{'bolsistas':bolsistas})



@login_required(login_url='/login')
def list_acesso(request):
	acessos = Acesso.objects.all()
	return render(request, 'acesso/list_acesso.html',{'acessos':acessos})

def test_acesso(request, pk):
	try:

		bolsista = Bolsista.objects.get(pk=pk)
		acesso = Acesso.objects.filter(bolsista=bolsista).order_by('-id').first()
		if acesso is not None:

			if acesso.hora_saida == None:
				acesso.hora_saida = timezone.now()
				acesso.save()
				redirect('app:list_acesso')
			else:
				novo_acesso = Acesso()
				novo_acesso.bolsista =  bolsista
				novo_acesso.data = date.today()
				novo_acesso.hora_entrada = timezone.localtime(timezone.now()).time()
				novo_acesso.save()
				redirect('app:list_acesso')	
		else:
			novo_acesso = Acesso()
			novo_acesso.bolsista =  bolsista
			novo_acesso.data = date.today()
			novo_acesso.hora_entrada = timezone.localtime(timezone.now()).time()
			novo_acesso.save()
			redirect('app:list_acesso')	
	except Bolsista.DoesNotExist:
		redirect('app:list_acesso')
	acessos = Acesso.objects.all()
	return render(request, 'acesso/list_acesso.html', {'acessos':acessos})