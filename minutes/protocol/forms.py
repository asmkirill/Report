from django.forms import ModelForm, Textarea
from .models import ProtocolData

from django import forms
from django.forms import formset_factory
from .models import ProtocolData

class ProtocolDataForm(forms.ModelForm):
    class Meta:
        model = ProtocolData
        fields = ['no', 'item', 'responsible', 'deadline', 'status']

ProtocolFormSet = formset_factory(ProtocolDataForm, extra=50)  # Создание formset с 50 дополнительными формами





class ProtocolDataAddLines(ModelForm):
    class Meta:
        model = ProtocolData
        fields = ['title', 'no', 'item', 'responsible', 'deadline', 'status', 'notes']

        widgets = {
            'no': Textarea(attrs={
                'class': 'protocol_fields_no',
                'placeholder': 'No', 'rows': 2
            }),
            'item': Textarea(attrs={
                'class': 'protocol_fields_item',
                'placeholder': 'Item', 'rows': 2
            }),
            'responsible': Textarea(attrs={
                'class': 'protocol_fields_responsible',
                'placeholder': 'Responsible', 'rows': 2
            }),
            'deadline': Textarea(attrs={
                'class': 'protocol_fields_deadline',
                'placeholder': 'Deadline', 'rows': 2
            }),
            'status': Textarea(attrs={
                'class': 'protocol_fields_status',
                'placeholder': 'Status', 'rows': 2
            }),
        }
