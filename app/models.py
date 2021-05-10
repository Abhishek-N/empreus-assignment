from django.db import models


class Classes(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=56)
    duration = models.IntegerField()
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
    img_url = models.URLField(default="")
    from_time_zone = models.TextField(max_length=8, default="")
    to_time_zone = models.TextField(max_length=8, default="")


class Meta:
    db_table = "classes"
