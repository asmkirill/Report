from .models import DocumentsIdentifier
from django.forms import ModelForm, TextInput
from django import forms


class DocumentIdentifierForm(ModelForm):
    class Meta:
        model = DocumentsIdentifier
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



class DocumentDataForm(forms.Form):
    identifier = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    def get_document_data(self):
        identifier = self.cleaned_data.get('identifier')
        document = DocumentsIdentifier.objects.filter(identifier=identifier).first()
        if document:
            return document
        return None



class DocumentIdentifierForm(forms.ModelForm):
    identifier = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = DocumentsIdentifier
        fields = ['identifier']