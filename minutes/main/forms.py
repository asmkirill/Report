from .models import DocumentsIdentifier
from django.forms import ModelForm, TextInput


class DocumentIdentifierForm(ModelForm):
    class Meta:
        model = DocumentsIdentifier
        fields = ['identifier']

        widgets = {
            'identifier': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Identifier of document',
            })
        }

