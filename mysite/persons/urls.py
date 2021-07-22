from django.urls import path

from . import views

app_name = 'persons'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:person_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('save/', views.save, name='save'),

]