from django.shortcuts import render ,redirect
from .forms import StudentForm ,UserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

# Create your views here.

def studentReg(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_form = UserForm(request.POST)
            student_form = StudentForm(request.POST)
            if user_form.is_valid() and student_form.is_valid():
                raw_password = user_form.cleaned_data.get('password')
                user = user_form.save(commit=False)
                user.set_password(raw_password)
                user.save()
                student = student_form.save(commit=False)
                student.username = user
                student.save()
                login(request,user)

                messages.success(request, "Account created successfully , Welcome ")

                return redirect('/')
        else:    
            user_form = UserForm()
            student_form = StudentForm()
        return render(request,'student/register.html', {'user_form' : user_form, 'student_form' :student_form })
    else:
        messages.error(request, 'you already logged !!!')
        return redirect('/')

def mycourses(request):
    student = request.user.student
    courses = student.classgroup_set.all()
    context = {"courses" : courses}
    return render(request,'student/mycourses.html',context)


