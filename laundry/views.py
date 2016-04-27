from django.shortcuts import render
import datetime
import calendar


from .models import *

# Create your views here.
def index(request, washroom_id=0):
    washrooms=Washroom.objects.all()
    hours=Hour.objects.all()
    today = datetime.date.today()
    cal = calendar.Calendar()
    schedules=Schedule.objects.filter(washroom_id=washroom_id,date__year=today.year,date__month=today.month)
    schedules_dict = {(s.date.day, s.time_id): s for s in schedules}
    days = [day for day in cal.itermonthdates(today.year, today.month) if day.month==today.month ]

    return render(request,"index.html",{'washrooms':washrooms, 'active':int(washroom_id),'hours':hours,'days':days,'schedules':schedules_dict})

