from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from app import views

app_name = 'app'

urlpatterns = [


	url(r'^$', views.home, name='home'),
	url(r'^relatorio/$', views.relatorio_op, name='relatorio_op'),
	url(r'^login/$', views.logar, name='logar'),
	url(r'^sair/$', auth_views.logout,{'next_page': 'app:logar'}, name='sair'),	
	
	#url(r'^teste/$', views.GeneratePdf.as_view(), name='GeneratePdf'),
	
	url(r'^acesso/relatorio_periodoB/(?P<data_ini>[\w.@+-]+)/(?P<data_fim>[\w.@+-]+)/(?P<pk>\d+)/$', views.RelatorioPeriodoB.as_view(), name='RelatorioPeriodoB'),

	url(r'^acesso/relatorio_bolsista/(?P<pk>\d+)$', views.RelatorioBolsista.as_view(), name='RelatorioBolsista'),
	url(r'^acesso/relatorio_periodo/(?P<data_ini>[\w.@+-]+)/(?P<data_fim>[\w.@+-]+)/$', views.RelatorioPeriodo.as_view(), name='RelatorioPeriodo'),


	url(r'^bolsista/$', views.list_bolsista, name='list_bolsista'),
    url(r'^bolsista/cad_bolsista/$', views.create_bolsista, name='create_bolsista'),	
	url(r'^bolsista/editar_bolsista/(?P<pk>\d+)$', views.update_bolsista, name='update_bolsista'),
	url(r'^bolsista/deletar_bolsista/(?P<pk>\d+)$', views.delete_bolsista, name='delete_bolsista'),
	url(r'^bolsista/list_bolsista/$', views.list_bolsista, name='list_bolsista'),

	url(r'^acessos/$', views.apb, name='apb'),
	url(r'^acesso/cad_acesso/$', views.create_ac, name='create_ac'),	
	url(r'^acesso/test_acesso/(?P<pk>\d+)$', views.test_acesso, name='test_acesso'),
	url(r'^acesso/relatorio_bolsista/(?P<pk>\d+)$', views.acesso_bolsista, name='acesso_bolsista'),
	url(r'^acesso/acesso_bolsista/$', views.ac, name='ac'),	
	url(r'^acesso/acesso_bolsista/$', views.act, name='act'),	

	url(r'^acesso/acesso_periodo/$', views.ap, name='ap'),	
	
#	url(r'^acesso/reg_entrada/(?P<pk>\d+)$', views.register_entrada, name='register_entrada'),
	url(r'^acesso/list_acesso/$', views.list_acesso, name='list_acesso'),
	url(r'^acesso/list_ap/(?P<data_ini>[\w.@+-]+)/(?P<data_fim>[\w.@+-]+)/$', views.list, name='list'),
	
	#url(r'^editar_movimentacao/$', views.update_movimentacao, name='update_movimentacao'),
    #url(r'^list_movimentacao/$', views.list_movimentacao, name='list_movimentacao'),
	url(r'^professor/$', views.list_professor, name='list_professor'),
	url(r'^professor/cad_professor/$', views.create_professor, name='create_professor'),	
	url(r'^professor/editar_professor/(?P<pk>\d+)$', views.update_professor, name='update_professor'),
	url(r'^professor/deletar_professor/(?P<pk>\d+)$', views.delete_professor, name='delete_professor'),
	url(r'^professor/list_professor/$', views.list_professor, name='list_professor'),   

]