from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from .forms import teacherLoginForm, teacherSignupForm, teacherSignupForm2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as auth_login,logout as auth_logout
from .models import teacherSignup
from student.models import studentSignup
from exam.models import courses,Question,result
from exam.forms import questionForm,coursesForm
# Create your views here.
class teacherLoginFormFunc(View):
    def get(self,request):
        login = teacherLoginForm()
        data = {'login':login}
        return render(request,'teacherLogin.html',data)

    def post(self,request):
        login = teacherLoginForm(request.POST)
        if login.is_valid():
            username = login.cleaned_data['teacherUserName']
            password = login.cleaned_data['teacherPassword']
            user=authenticate(username=username,password=password)
            if user is not None:
                var = teacherSignup.objects.get(username = username)
                if var.active == False:
                    return render(request,'teacherBlock.html')
                else:
                    auth_login(request,user)
                    return redirect('teacherDashboard')
            else:
                return HttpResponse("wrong")

class teacherSignupFormFunc(View):
    def get(self,request):
        signup = teacherSignupForm()
        signup2 = teacherSignupForm2()
        d = {'signup':signup,'signup2':signup2}
        return render(request,'teacherSignUp.html',d)
    def post(self,request):
        data = teacherSignupForm(request.POST,request.FILES)
        if data.is_valid():
            data = teacherSignupForm(request.POST,request.FILES)
            data2 = teacherSignupForm2(request.POST)
        if data.is_valid() and data2.is_valid():
            try:
                uname = data.cleaned_data['username']
                pas = data2.cleaned_data['teacherPassword']
                user=User.objects.create_user(username=uname,password=pas)
                user.save()
                data.save()
                return redirect('teacherLogin')
            except:
                return render(request,'error.html')


def teacherLogout(request):
    auth_logout(request)
    return redirect('teacherLogin')

class teacherDashboard(View):
    def get(self,request):
        z = request.user
        data = teacherSignup.objects.get(username = z)
        studentCount = studentSignup.objects.all().count()
        course = courses.objects.all().count()
        question = Question.objects.all().count()
        results = result.objects.all()
        d ={
            'data':data,
            'studentCount':studentCount,
            'course':course,
            'question':question,
            'results':results,
        }
        return render(request,'teacherDashboard.html',d)

class teacherCourse(View):
    def get(self,request):
        z = request.user
        data = teacherSignup.objects.get(username = z)
        form = coursesForm()
        totalCourses = courses.objects.all().count()
        d = {
            'data':data,
            'course':form,
            'totalCourses':totalCourses,
        }
        return render(request,'teacherCourse.html',d)

    def post(self, request):
        form = coursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacherCourse')

class teacherAddQuestion(View):
    def get(self,request):
        z = request.user
        data = teacherSignup.objects.get(username = z)
        form = questionForm()
        totalQuestion = Question.objects.all().count()
        d = {
            'data':data,
            'question':form,
            'totalQuestion':totalQuestion,
        }
        return render(request,'teacherAddQuestion.html',d)
    
    def post(self, request):
        form = questionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacherAddQuestion')
