from django.forms import ModelForm, TextInput, Textarea
from .models import ProtocolData


class ProtocolDataForm(ModelForm):
    class Meta:
        model = ProtocolData
        fields = ['title', 'no', 'item', 'responsible', 'deadline', 'status', 'notes']

        widgets = {
            'title': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Title of meeting'
            }),

            'no': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'No'
            }),
            'item': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Item'
            }),
            'responsible': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Responsible'
            }),
            'status': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Status'
            }),
            'notes': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Other notes'
            })
        }

