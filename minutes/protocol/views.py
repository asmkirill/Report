from django.shortcuts import render, redirect
from .forms import ProtocolData, ProtocolDataForm


def create_protocol(request, id):
    # находим документ по id
    try:
        documents_identifier = DocumentsIdentifier.objects.get(id=id)
    except DocumentsIdentifier.DoesNotExist:
        return HttpResponseNotFound('Document not found')
    # генерируем форму создания протокола с данными из найденного документа
    form = ProtocolDataForm(initial={'title': documents_identifier.title})
    data = {
        'form': form,
        'documents_identifier': documents_identifier
    }
    return render(request, 'protocol/create_protocol.html', data)



