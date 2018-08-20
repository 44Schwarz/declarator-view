from django.urls import path
from . import views

app_name = 'declarator'
urlpatterns = [
    path('', views.show_table),
    path('office/<of_id>/', views.offices, name='office')

]
