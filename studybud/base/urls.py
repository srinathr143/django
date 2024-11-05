from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.loginPage,name = 'login'),
    path('logout/',views.logoutUser,name = 'logout'),
    path('register/',views.registerUser,name = 'register'),
    path('profile/<str:pk>/',views.userProfile, name=' user-profile' ),
    path('',views.home, name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('delete-message/<str:pk>',views.DeleteMessage,name ='delete-message'),
    path('create-room',views.CreateRoom,name='create-room'),
    path('update-room/<str:pk>',views.UpdateRoom,name='update-room'),
    path('delete-room/<str:pk>',views.DeleteRoom,name='delete-room'),
    
]