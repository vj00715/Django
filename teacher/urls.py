from django.urls import path
from . import views

urlpatterns = [
    path('',views.teacherLoginFormFunc.as_view(),name='teacherLogin'),
    path('teacherSignUp',views.teacherSignupFormFunc.as_view(),name='teacherSignUp'),
    path('teacherLogout',views.teacherLogout,name='teacherLogout'),

    path('teacherDashboard',views.teacherDashboard.as_view(),name='teacherDashboard'),
    path('teacherCourse',views.teacherCourse.as_view(),name='teacherCourse'),
    path('teacherAddQuestion',views.teacherAddQuestion.as_view(),name='teacherAddQuestion'),
]