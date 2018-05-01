from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from app import views

app_name = 'app'

urlpatterns = [


	url(r'^$', views.home, name='home'),
	url(r'^login/$', views.logar, name='logar'),
	url(r'^sair/$', auth_views.logout,{'next_page': 'app:logar'}, name='sair'),	
	
	url(r'^bolsista/$', views.list_bolsista, name='list_bolsista'),
    url(r'^bolsista/cad_bolsista/$', views.create_bolsista, name='create_bolsista'),	
	url(r'^bolsista/editar_bolsista/(?P<pk>\d+)$', views.update_bolsista, name='update_bolsista'),
	url(r'^bolsista/deletar_bolsista/(?P<pk>\d+)$', views.delete_bolsista, name='delete_bolsista'),
	url(r'^bolsista/list_bolsista/$', views.list_bolsista, name='list_bolsista'),

	url(r'^acesso/cad_acesso/(?P<pk>\d+)$', views.create_acesso, name='create_acesso'),
	#url(r'^editar_movimentacao/$', views.update_movimentacao, name='update_movimentacao'),
    #url(r'^list_movimentacao/$', views.list_movimentacao, name='list_movimentacao'),
	url(r'^professor/$', views.list_professor, name='list_professor'),
	url(r'^professor/cad_professor/$', views.create_professor, name='create_professor'),	
	url(r'^professor/editar_professor/(?P<pk>\d+)$', views.update_professor, name='update_professor'),
	url(r'^professor/deletar_professor/(?P<pk>\d+)$', views.delete_professor, name='delete_professor'),
	url(r'^professor/list_professor/$', views.list_professor, name='list_professor'),   

]