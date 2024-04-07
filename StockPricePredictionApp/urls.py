from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('student/',views.student,name='student'),
    path('explainable/',views.explainable,name='explainable'),
    path('home/',views.home,name='home'),
    path('home1/',views.home1,name='home1'),
    path('compare/',views.compare,name='compare'),
    path('compare1/',views.compare1,name='compare1'),
    path('download/<id>',views.download,name='download'),
    path('predict/',views.predict,name='predict'),
    path('predict1/',views.predict1,name='predict1'),
    path('all_stocks/',views.all_stocks,name='all_stocks'),
    path('all_stocks1/',views.all_stocks1,name='all_stocks1'),
    path('details/<id>',views.details,name='details'),
   
]