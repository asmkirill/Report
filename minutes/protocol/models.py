from django.db import models


class ProtocolData(models.Model):
    title = models.CharField('Name of title', max_length=200)
    no = models.CharField('No', max_length=10)
    item = models.TextField('Item')
    responsible = models.TextField('Responsible')
    deadline = models.TextField('Deadline')
    status = models.TextField('Item')
    notes = models.TextField('Other notes', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Protocol data'
        verbose_name_plural = 'Protocol data'



