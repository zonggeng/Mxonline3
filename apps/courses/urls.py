from courses.views import CourseListView

from django.urls import path, re_path

app_name = "courses"

urlpatterns = [
    # 课程列表url
    path('list/', CourseListView.as_view(), name="list"),
]
