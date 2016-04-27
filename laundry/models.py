from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Washroom(models.Model):
    name=models.CharField(max_length=64)
    order=models.IntegerField()

    def __str__(self):
        return self.name.encode("utf-8")

class Hour(models.Model):
    time_start=models.TimeField()
    time_end=models.TimeField()

    def __str__(self):
        return " - ".join(t.strftime("%H:%M") for t in (self.time_start, self.time_end))

class Schedule(models.Model):
    room=models.CharField(max_length=8)
    washroom = models.ForeignKey(Washroom, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.ForeignKey(Hour, on_delete=models.CASCADE)

    def __str__(self):
        return self.room.encode("utf8")



