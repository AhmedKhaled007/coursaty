from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Course ,Instructor ,ClassGroup , Track
from django.contrib import messages

# Create your views here.

def list_course(request):
    courses = list(Course.objects.all())
    tracks = Track.objects.all()
    context = {"mycourses" : courses, "tracks" : tracks}
    return render(request, 'courses/courses.html', context)


def course_class(request,course_id):
    course = get_object_or_404(Course, pk = course_id) 
    course_groups = course.classgroup_set.all()
    context = {"course_groups" : course_groups , "course" : course}
    return render(request,'courses/classes.html', context)

def course_details(request,course_id):
    course = get_object_or_404(Course, pk = course_id) 
    context = { "course" : course}
    return render(request,'courses/course_details.html', context)
    

def enrollment(request,group_id):
    if request.user.is_authenticated:
        student = request.user.student
        group = ClassGroup.objects.get(pk=group_id)
        group.students.add(student)
        messages.success(request,'Congaration You Successfully Enrollment in course')
        return redirect('studentcourses')
    else:
        messages.error(request, 'You need to login First.')
        return redirect('login')



def track_details(request,track_id):
    track = get_object_or_404(Track , pk = track_id)
    track_courses = track.courses.all()
    context = {"track_courses" : track_courses , "track":track}
    return render (request , 'courses/track-details.html', context)