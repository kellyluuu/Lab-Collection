from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    path('races/', views.races_index, name='index'),
    path('races/<int:race_id>/', views.races_detail, name='detail'),
    path('races/create/', views.RaceCreate.as_view(), name='races_create'),
    path('races/<int:pk>/update/', views.RaceUpdate.as_view(), name= 'races_update'),
    path('races/<int:pk>/delete/', views.RaceDelete.as_view(), name='races_delete'),
    
    # add training 
    path('races/<int:race_id>/add_training/', views.add_training, name='add_training'),
    
    path('completed/', views.CompletedList.as_view(), name='completed_index'),
    path('completed/<int:pk>/', views.CompletedDetail.as_view(), name='completed_detail'),
    path('completed/create/', views.CompletedCreate.as_view(), name='completed_create'),
    path('completed/<int:pk>/update/', views.CompletedUpdate.as_view(), name='completed_update'),
    path('completed/<int:pk>/delete/', views.CompletedDelete.as_view(), name='completed_delete'),
    
    path('races/<int:race_id>/assoc_completed/<int:completed_id>/', views.assoc_completed, name='assoc_completed'),
    ]

