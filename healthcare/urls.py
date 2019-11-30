
from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('register/', views.register, name='register'),

    path('student_login/', views.Student_login, name='student_login'),
    path('go_live/', views.sucess, name='sucess'),
    path('user_logout/', views.user_logout, name='user_logout'),
]
