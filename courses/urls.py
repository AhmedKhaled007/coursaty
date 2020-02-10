from django.urls import path
from . import views


urlpatterns = [
    path("",views.list_course, name ="courses"),
    path("enroll/<int:group_id>",views.enrollment, name ="enroll"),
    path("<int:course_id>/classes", views.course_class, name="course_class"),
    path("<int:course_id>/", views.course_details, name="course_details"),
    path("track/<int:track_id>/", views.track_details, name="track_details"),
]