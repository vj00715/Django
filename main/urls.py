from django.urls import path
from . import views

urlpatterns = [
    path('',views.masterLoginFormFunc.as_view(),name='masterLogin'),
    path('masterSignUp',views.masterSignupFormFunc.as_view(),name='masterSignUp'),
    path('masterLogout',views.masterLogout,name='masterLogout'),
    
    path('masterDashboard',views.masterDashboard.as_view(),name='masterDashboard'),
    path('masterTeacher',views.masterTeacher.as_view(),name='masterTeacher'),
    path('masterStudent',views.masterStudent.as_view(),name='masterStudent'),
    path('masterCourse',views.masterCourse.as_view(),name='masterCourse'),
    path('masterAddQuestion',views.masterAddQuestion.as_view(),name='masterAddQuestion'),
    path('approve/<int:pk>',views.approve,name='approve'),
    path('block/<int:pk>',views.block,name='block'),
]