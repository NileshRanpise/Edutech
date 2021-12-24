
from django.urls import path
from . import views



urlpatterns = [
   

    path('register/',views.registerPage,name='register'),
    path('',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('home/', views.home,name='home' ),
    # path('student/', views.student,name='student' ),
    path('student/<str:pk>/', views.student,name='student' ),
    path('teacher/<str:pk>/', views.teacher,name='teacher' ),
    path('student/', views.StudentPage,name='studentpage' ),
    path('teacher/', views.TeacherPage,name='teacherpage' ),
    
    
] 
