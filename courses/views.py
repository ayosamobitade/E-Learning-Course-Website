from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import Course

class ManageCourseListView(ListView)
    model = Course
    template_name = 'courses/manage/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
