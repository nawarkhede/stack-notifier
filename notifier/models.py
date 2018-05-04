from django.db import models


class StackOverflow(models.Model):
    question_id = models.BigIntegerField()
    title = models.CharField(max_length=500)
    summary = models.CharField(max_length=2000)
    href = models.URLField()

    def __unicode__(self):
        return '%s' % self.title
