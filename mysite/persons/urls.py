from django.urls import path

from . import views

app_name = 'persons'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:person_id>/', views.detail, name='detail'),
    path('new/<int:person_id>/', views.new, name='new'),
    path('upd/<int:person_id>/', views.upd, name='upd'),
    path('save/', views.save, name='save'),
    path('put/<int:person_id>', views.put, name='put'),
    path('del/<int:person_id>', views.delete, name='del'),
    

]