from django.db import models
import datetime

class Status(models.Model):
    on_off = models.BooleanField(default=True)
    last_start = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

    def __unicode__(self):
        return '%s %s' % (self.on_off, self.last_start)


    
