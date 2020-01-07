from account import models
from .models import Courses, Record
from django import forms


class RecordForm(forms.ModelForm):
    st_mtrl = forms.CharField()
    course_code = forms.CharField()
    status = forms.BooleanField()


    class Meta:
        model = Record
        fields = ('st_mtrl','course_code','status',)

