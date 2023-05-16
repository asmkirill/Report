from django.db import models


from django import forms
from django.forms import formset_factory

class ProtocolForm(forms.Form):
    no = forms.CharField(label='No', max_length=40, required=False)
    item = forms.CharField(label='Item', max_length=1000)
    responsible = forms.CharField(label='Responsible', max_length=100, required=False)
    deadline = forms.CharField(label='Deadline', max_length=100, required=False)
    status = forms.CharField(label='Status', max_length=100, required=False)

ProtocolFormSet = formset_factory(ProtocolForm, extra=50, can_delete=True)




class ProtocolDataAddLines(models.Model):
    no = models.TextField('No', max_length=40, blank=True, null=True)
    item = models.TextField('Item', max_length=1000)
    responsible = models.TextField('Responsible', max_length=100, blank=True, null=True)
    deadline = models.TextField('Deadline', max_length=100, blank=True, null=True)
    status = models.TextField('Status', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.item
