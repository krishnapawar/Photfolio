from django.urls import path
from.import views

urlpatterns=[
path('home/',views.myjobs,name='hindex'),
path('<int:bid>/',views.bdm,name='bdaetaile'),
]