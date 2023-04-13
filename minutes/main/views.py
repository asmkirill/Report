from django.shortcuts import render, redirect
from .forms import DocumentIdentifierForm, DocumentDataForm
from .models import DocumentsIdentifier
from django.http import HttpResponseBadRequest
from django.template.loader import render_to_string


def about(request):
   return render(request, 'main/about.html')




def index(request):
    error = ''
    if request.method == 'POST':
        form = DocumentDataForm(request.POST)
        if form.is_valid():
            # Получаем данные из формы
            identifier = form.cleaned_data['identifier']
            # Ищем документ по идентификатору
            document = DocumentsIdentifier.objects.filter(identifier=identifier).first()
            if document:
                data = {
                    'document': document,
                    'fields': {
                        'field_1': 'number',
                        'field_2': 'item',
                        'field_3': 'status',
                        'field_4': 'description'
                    }
                }
                return render(request, 'main/document_data.html', data)
            else:
                error = 'Document not found'
        else:
            error = 'Wrong input'







def get_data(request):
    form = DocumentDataForm(request.GET or None)
    data = {}
    if form.is_valid():
        document = form.get_document_data()
        if document:
            data = {
                'title': 'Document data',
                'document': document,
            }
    return render(request, 'main/document_data.html', {'form': form, **data})


