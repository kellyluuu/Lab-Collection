from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('races/', views.races_index, name='index'),
    path('races/<int:race_id>/', views.races_detail, name='detail'),
    path('races/create/', views.RaceCreate.as_view(), name='races_create'),
    path('races/<int:pk>/update/', views.RaceUpdate.as_view(), name= 'races_update'),
    path('races/<int:pk>/delete/', views.RaceDelete.as_view(), name='races_delete')
]