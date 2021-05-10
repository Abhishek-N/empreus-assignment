from django.db import models


class Classes(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=16)
    duration = models.DurationField()
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()

class Meta:
    db_table = "classes"