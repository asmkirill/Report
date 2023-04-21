from django import forms
from django.forms import ModelForm, Textarea, BaseFormSet
from .models import ProtocolData


class ProtocolDataForm(ModelForm):
    class Meta:
        model = ProtocolData
        fields = ['title', 'no', 'item', 'responsible', 'deadline', 'status', 'notes']

        widgets = {
            'title': Textarea(attrs={
                'class': 'protocol_fields_title',
                'placeholder': 'Title', 'rows': 2
            }),
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
            'notes': Textarea(attrs={
                'class': 'protocol_fields_notes',
                'placeholder': 'Other notes', 'rows': 2
            })
        }


