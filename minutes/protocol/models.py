from django.db import models


class ProtocolData(models.Model):
    title = models.TextField('Name of title', max_length=200, blank=True, null=True)
    no = models.TextField('No', max_length=40, blank=True, null=True)
    item = models.TextField('Item', max_length=1000)
    responsible = models.TextField('Responsible', max_length=100, blank=True, null=True)
    deadline = models.TextField('Deadline', max_length=100, blank=True, null=True)
    status = models.TextField('Status', max_length=100, blank=True, null=True)
    notes = models.TextField('Other notes', max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Protocol data'
        verbose_name_plural = 'Protocol data'
