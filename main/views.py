from itertools import count
from sqlite3 import Row
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import masterSignupForm, masterLoginForm, masterSignupForm2
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as auth_login,logout as auth_logout
from .models import masterSignup
from teacher.models import teacherSignup
from student.models import studentSignup
from main.models import masterSignup
from exam.forms import coursesForm,questionForm
from exam.models import courses,Question


# Create your views here.
# master signup
# ------------------------------------------------Sign up----------------------------------------------------------
class masterSignupFormFunc(View):
    def get(self, request):
        signup = masterSignupForm()
        signup2 = masterSignupForm2()
        d = {'signup': signup,'signup2': signup2}
        return render(request, 'masterSignUp.html', d)
    def post(self, request):
        data = masterSignupForm(request.POST,request.FILES)
        data2 = masterSignupForm2(request.POST)
        if data.is_valid() and data2.is_valid():
            try:
                uname = data.cleaned_data['username']
                pas = data2.cleaned_data['mainPassword']
                user=User.objects.create_user(username=uname,password=pas)
                user.save()
                data.save()
                return redirect('masterLogin')
            except:
                return render(request,'error.html')

# ------------------------------------------------Login----------------------------------------------------------
#masterLogin
class masterLoginFormFunc(View):
    def get(self, request):
        login = masterLoginForm()
        d = {'login': login}
        return render(request, 'masterLogin.html', d)

    def post(self,request):
        login = masterLoginForm(request.POST)
        if login.is_valid():
            username = login.cleaned_data['masterUserName']
            password = login.cleaned_data['masterPassword']
            user=authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('masterDashboard')
            else:
                return HttpResponse("wrong")

# ------------------------------------------------Logout----------------------------------------------------------
def masterLogout(request):
    auth_logout(request)
    return redirect('masterLogin')

# ------------------------------------------------DasBoard----------------------------------------------------------
class masterDashboard(View):
    def get(self, request):
        z = request.user
        data = masterSignup.objects.get(username = z)
        teacherCount = teacherSignup.objects.all().count()
        studentCount = studentSignup.objects.all().count()
        totalCourses = courses.objects.all().count()
        totalQuestion = Question.objects.all().count()

        masterAll = masterSignup.objects.all()
        teacherAll = teacherSignup.objects.all()
        d = {
            'data':data,
            'teacherCount':teacherCount,
            'studentCount':studentCount,
            'masterAll': masterAll,
            'teacherAll': teacherAll,
            'totalCourses':totalCourses,
            'totalQuestion':totalQuestion,
            }
        return render(request,'masterDashboard.html',d)
    def post(self,request):
        pass

# ------------------------------------------------Teacher----------------------------------------------------------
class masterTeacher(View):
    def get(self, request):
        z = request.user
        data = masterSignup.objects.get(username = z)
        activeTeacher = teacherSignup.objects.filter(active = True).count()
        pendingTeacher = teacherSignup.objects.filter(active = False).count()
        pendingTeacherDisApprove = teacherSignup.objects.filter(active = True)
        pendingTeacherApprove = teacherSignup.objects.filter(active = False)
        totalSalary = teacherSignup.objects.all()
        z = 0
        for i in totalSalary:
            z += i.salary

        d = {
            'pendingTeacherDisApprove':pendingTeacherDisApprove,
            'pendingTeacherApprove':pendingTeacherApprove,
            'pendingTeacher':pendingTeacher,
            'activeTeacher':activeTeacher,
            'data': data,
            'totalSalary': z,
        }
        return render(request,'masterTeacher.html',d)

def approve(request,pk):
    if request.method=='POST':
        try:
            z = teacherSignup.objects.get(id = pk)
            salary = request.POST['teacherSalary']
            z.salary = salary
            z.active = True
            z.save()
            return redirect('masterTeacher')
        except:
            return redirect('masterTeacher')

def block(request,pk):
    z = teacherSignup.objects.get(id = pk)
    z.active = False
    z.salary = 0
    z.save()
    return redirect('masterTeacher')



# ------------------------------------------------Student----------------------------------------------------------
class masterStudent(View):
    def get(self, request):
        z = request.user
        data = masterSignup.objects.get(username = z)
        studentAll = studentSignup.objects.all()
        studentCount = studentSignup.objects.all().count()
        d = {
            'data':data,
            'studentCount': studentCount,
            'studentAll':studentAll,
        }
        return render(request,'masterStudent.html',d)

# ------------------------------------------------Course---------------------------------------------------------
class masterCourse(View):
    def get(self, request):
        z = request.user
        data = masterSignup.objects.get(username = z)
        form = coursesForm()
        totalCourses = courses.objects.all().count()
        d = {
            'data':data,
            'course':form,
            'totalCourses':totalCourses,
        }
        return render(request,'masterCourse.html',d)

    def post(self, request):
        form = coursesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('masterCourse')

# ------------------------------------------------AddQuestion----------------------------------------------------------
class masterAddQuestion(View):
    def get(self, request):
        z = request.user
        data = masterSignup.objects.get(username = z)
        form = questionForm()
        totalQuestion = Question.objects.all().count()
        d = {
            'data':data,
            'question':form,
            'totalQuestion':totalQuestion,
        }
        return render(request,'masterAddQuestion.html',d)
    
    def post(self, request):
        form = questionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('masterAddQuestion')