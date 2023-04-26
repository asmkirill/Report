from .models import DocumentsIdentifier
from django.forms import ModelForm, TextInput


class DocumentIdentifierForm(ModelForm):
    class Meta:
        model = DocumentsIdentifier
        fields = ['identifier']

        widgets = {
            'identifier': TextInput(attrs={
                'class': 'identifier_input',
                'placeholder': 'Identifier of document',
            })
        }

