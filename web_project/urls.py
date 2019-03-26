from django.contrib import admin
from django.urls import path

from workforceapp import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('/',views.header),

    path('home/macroWfp',views.homemacro,name='macroWfp'),

    path('home/macro/cfumobile',views.cfumobile,name='cfumobile'),
    path('home/macro/cfuconsumer',views.cfuconsumer,name='cfuconsumer'),
    path('home/macro/cfuenterprise',views.cfuenterprise,name='cfuenterprise'),
    path('home/macro/cfuwib',views.cfuwib,name='cfuwib'),
    path('home/macro/fudsp',views.fudsp,name='fudsp'),
    path('home/macro/funits',views.funits,name='funits'),
    path('home/macro/fufinance',views.fufinance,name='fufinance'),
    path('home/macro/fuhcm',views.fuhcm,name='fuhcm'),
    path('home/macro/ceooffice',views.ceooffice,name='ceooffice'),

    path('home/microWfp',views.homemicro,name='microWfp'),
    
    path('Process/',views.process,name='process'),

    path('WFPHelpCenter/ubs',views.helpcenterubs,name='ubs'),
    path('WFPHelpCenter/dcs',views.helpcenterdcs,name='dcs'),
    path('WFPHelpCenter/mne',views.helpcenterdcs,name='mne'),
    path('WFPHelpCenter/icn',views.helpcentericn,name='icn'),
    path('WFPHelpCenter/dap',views.helpcenterdap,name='dap'),
    path('WFPHelpCenter/contact',views.helpcentercontact,name='contact'),
]
