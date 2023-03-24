from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .forms import studentSignupForm, studentLoginForm, contactForm,studentSignupForm2
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as auth_login,logout as auth_logout
from .models import studentSignup
from exam.models import courses,Question,result

# Create your views here.
#signup
class studentSignupFormFunc(View):
    def get(self,request):
        signup = studentSignupForm()
        signup2 = studentSignupForm2()
        d = {'studentSignup': signup,'studentSignup2': signup2}
        return render(request,'studentSignUp.html',d)
    def post(self,request):
        data = studentSignupForm(request.POST,request.FILES)
        data2 = studentSignupForm2(request.POST)
        if data.is_valid() and data2.is_valid():
            try:
                uname = data.cleaned_data['username']
                pas = data2.cleaned_data['studentPassword']
                user=User.objects.create_user(username=uname,password=pas)
                user.save()
                data.save()
                return redirect('studentLogin')
            except:
                return render(request,'error.html')
# #######################################################################################################
#login home
class studentLoginFormFunc(View):
    def get(self,request):
        login = studentLoginForm()
        d={'login':login}
        return render(request,'studentLogin.html',d)
    
    def post(self,request):
        login = studentLoginForm(request.POST)
        if login.is_valid():
        #studentUserName,studentPassword
            username = login.cleaned_data['studentUserName']
            password = login.cleaned_data['studentPassword']
            user=authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('studentDashboard')
            else:
                return HttpResponse("wrong")
##################################################################################################################

def studentLogout(request):
    auth_logout(request)
    return redirect('studentLogin')


###########################################################################################
#contact
class contactFormFunc(View):
    def get(self,request):
        contact = contactForm()
        d ={'contact':contact}
        return render(request,'contact.html',d)
    def post(self,request):
        contact = contactForm(request.POST)
        if contact.is_valid():
            contact.save()
            # messages.success(request, 'Your Request has Been Successfully Recorded!!!!')
            return redirect('contact')

##################################################################################################

class studentDashboard(View):
    def get(self,request):
        z = request.user
        data = studentSignup.objects.get(username = z)
        totalCourses = courses.objects.all().count()
        d = {
            'data':data,
            'totalCourses':totalCourses,
        }
        return render(request,'studentDashboard.html',d)

class studentExam(View):
    def get(self,request):
        z = request.user
        data = studentSignup.objects.get(username = z)
        course = courses.objects.all()
        d = {
            'data':data,
            'course':course,
        }
        return render(request,'studentExam.html',d)


class studentResult(View):
    def get(self,request):
        z = request.user
        data = studentSignup.objects.get(username = z)
        marks = result.objects.filter(username=z)
        d = {
            'data':data,
            'marks':marks,
        }
        return render(request,'studentResult.html',d)




class question(View):
    def get(Self,request,course):
        z = request.user
        data = studentSignup.objects.get(username = z)
        que = Question.objects.filter(courseQuestion = course)
        d = {
            'data':data,
            'que':que,
        }
        return render(request,'studentExam2.html',d)

    def post(Self,request,course):
        no_of_question = Question.objects.filter(courseQuestion = course).count()
        que = Question.objects.filter(courseQuestion = course)
        username = request.user
        c = course
        total = courses.objects.get(courseName = course).questionMarks
        count = 0
        for i in que:
            id = i.id
            choice = request.POST[str(id)]
            ans = i.answer
            if ans == choice:
                count +=1
        studentMarks = (total/no_of_question)*count
        res = result(username=username,course=c,totalMarks=total,studentMarks=studentMarks)
        res.save()
        return redirect('studentResult')