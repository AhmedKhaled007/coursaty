from django.db import models
from inst.models import Instructor
from student.models import Student
from datetime import datetime, timedelta
from .utlis import SortWeek
from django.db.models.signals import post_save ,m2m_changed
from django.dispatch import receiver

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_hours = models.IntegerField()
    course_price = models.IntegerField(default=0)
    course_cover = models.ImageField(upload_to = 'profile' , blank=True)
    def __str__(self):
        return self.course_name


class Weekday(models.Model):
    Week = models.IntegerChoices('Week','Monday Tuesday Wednesday Thursday Friday Saturday Sunday')
    days = models.SmallIntegerField(choices = Week.choices,unique=True)
    def __str__(self):
        return f' {self.get_days_display()} '

#course instance 
class ClassGroup(models.Model):
    class_Instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT )
    start_date = models.DateField()
    end_date = models.DateField()
    session_count = models.IntegerField()   
    days = models.ManyToManyField(Weekday)
    students = models.ManyToManyField(Student, through = 'Enrollment' )
    

    def generateSessionsdate(self):
        # cor = self.course
        sessionCount = self.session_count 
        startdate = self.start_date 
        weekdays = list(self.days.all())
        daysarr = []
        for day in weekdays:
            daysarr.append(day.days)
        startday = startdate.isoweekday()
        daysarr = SortWeek(daysarr,startday)
        sessiondate = startdate
        Session.objects.create(session_date = sessiondate , course = self)        
        sessionc = 1
        while sessionc < sessionCount:
            for i,day in enumerate(daysarr):
                thisday = day
                nextday = daysarr[(i+1) % len(daysarr)]
                if nextday < thisday :
                    dt = nextday+7 - thisday
                else :
                    dt = nextday-thisday
                sessiondate +=  timedelta(days = dt)
                Session.objects.create(session_date = sessiondate , course = self)
                sessionc += 1
    def __str__(self):
        return f"{self.course}" 


class Enrollment(models.Model):
    student_enroll = models.ForeignKey(Student, on_delete=models.PROTECT)
    course_enroll = models.ForeignKey(ClassGroup, on_delete= models.PROTECT)
    date_enroll = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"enrollment id : {self.student_enroll.username.username} {self.course_enroll.course} "


class Track(models.Model):
    courses = models.ManyToManyField(Course)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    track_cover = models.ImageField(upload_to = 'profile' , blank=True)


    def __str__(self):
        return self.name


class Session(models.Model):
    course = models.ForeignKey(ClassGroup,on_delete=models.CASCADE)
    session_date = models.DateField()
    # start_time = models.TimeField()
    def __str__(self):
        return f"Session ID ={self.id}, Class = {self.course}, Date = {self.session_date.strftime('%a %d %b')}"

@receiver(m2m_changed , sender=ClassGroup.days.through)
def gene(sender, instance, action, **kwargs):
    if action == "post_add":
        instance.generateSessionsdate()
