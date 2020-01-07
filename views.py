import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from account.forms import RecordForm
from .models import Student
from .models import Courses
from .models import Record
from .models import StudentCourses


@login_required(login_url='Users/login')
def attendance(request):
    p = {}
    today = {}
    if not request.user.is_authenticated:
        return render(request, 'Users:login.html', {"message": " you mustlogin here please"})

    if 'course_code' in request.GET:
        print('gggggg')
        course_code = request.GET.get('course_code')
        level = request.GET.get('level')
        p = StudentCourses.objects.all().filter(Q(course_code=course_code) & Q(st_mtrl__level=level))
        print('zzzzz', p)
        now = datetime.datetime.now()
        today = datetime.date.today().strftime('%Y-%M-%D')
        print(today)

               

    return render(request, "blank-page.html",
                  {"courses": Courses.objects.all().filter(teachers__user=request.user),
                   "course": request.GET.get('course_code'), "p": p, "today": today})


def record(request, course):
    today = datetime.datetime.now()
    print(course)
    if Record.objects.all().filter(Q(course_code__course_code=course)& Q(date__year=today.year) & Q(date__day=today.day)):
        record='THIS ATTENDANCE FOR THIS DAY ALREADY EXIST'
        return render(request, "consult-attendance.html", {"message": record} )

    else:
        if request.method == 'POST':
            course = Courses.objects.get(course_code=course)

            for s in Student.objects.all():
                print(request.POST.get(str(s)))
                if request.POST.get(str(s)):
                    state = request.POST.get(str(s))
                    new_Record, new = Record.objects.get_or_create(
                        st_mtrl=s,
                        course_code=course,
                        status=True if (str(state) == 'on') else False
                    )
                else:
                    print(s)
            record = Record.objects.all()
            return render(request, "consult-attendance.html", {"Record": record} )


        else:
            form = RecordForm()


@login_required(login_url="login")
def consult(request):
    return render(request, "consult-attendance.html")
