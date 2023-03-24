from django.urls import path
from . import views

urlpatterns = [
   path('',views.studentLoginFormFunc.as_view(),name='studentLogin'),
   path('studentSignUp',views.studentSignupFormFunc.as_view(),name='studentSignUp'),
   path('contact',views.contactFormFunc.as_view(),name='contact'),
   path('studentLogout',views.studentLogout,name='studentLogout'),

   path('studentDashboard',views.studentDashboard.as_view(),name='studentDashboard'),
   path('studentExam',views.studentExam.as_view(),name='studentExam'),
   path('studentResult',views.studentResult.as_view(),name='studentResult'),
   path('question/<str:course>',views.question.as_view(),name='question')
]