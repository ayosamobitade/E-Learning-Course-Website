from django import forms
from courses.models import Course

class CourseEnrollForm(forms.Fomr):
    course = forms.ModelChoiceField(queryset = Course.objects.all(),
                                    widget=forms.HiddenInput)
    
    