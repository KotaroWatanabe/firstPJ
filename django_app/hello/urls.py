# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('create', views.create, name='create'),
        path('edit/<int:num>', views.edit, name='edit'),
        path('delete/<int:num>', views.delete, name='delete'),

#--------START
        # path('mainpage', views.mainpage, name='mainpage'),
        # path('detailpj', views.detailpj, name='detailpj'),
        # path('yourprof', views.yourprof, name='yourprof'),
        # path('jfinal', views.jfinal, name='jfinal'),
        # path('loginpage', views.loginpage, name='loginpage'),
        # path('mypage', views.mypage, name='mypage'),
        # path('makepj', views.makepj, name='makepj'),
        # path('jlist', views.jlist, name='jlist'),
        # path('wantlist', views.wantlist, name='wantlist'),
        # path('makeprof', views.makeprof, name='makeprof'),
        # path('jhlist', views.jhlist, name='jhlist'),
        # path('jreal', views.jreal, name='jreal'),
        # path('mdlreview', views.mdlreview, name='mdlreview'),
        # path('finreview', views.finreview, name='finreview'),
        # path('bothreview', views.bothreview, name='bothreview'),
        # path('hreal', views.hreal, name='hreal'),
] 