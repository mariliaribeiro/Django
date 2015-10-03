#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
	(r'^$', 'validacao.views.index'),
	(r'^valida/$', 'validacao.views.valida_cpf'),
    (r'^gera/$', 'validacao.views.gera_cpf'),
    (r'^gera_lista/$', 'validacao.views.gera_lista_cpf'),

    # url(r'^$', 'valida_cpf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
