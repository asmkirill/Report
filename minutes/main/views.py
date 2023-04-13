from django.shortcuts import render, redirect
from .forms import DocumentIdentifierForm
from .models import DocumentsIdentifier


def index(request):
    error = ''
    if request.method == 'POST':
        form = DocumentIdentifierForm(request.POST)
        if form.is_valid():
            # вместо сохранения формы выполняем поиск документа по номеру
            identifier = form.cleaned_data['identifier']
            try:
                documents_identifier = DocumentsIdentifier.objects.get(identifier=identifier)
            except DocumentsIdentifier.DoesNotExist:
                error = 'Document not found'
            else:
                # если документ найден, переходим на страницу создания протокола
                return redirect('create_protocol', id=documents_identifier.id)
        else:
            error = 'Document not found'
    else:
        # если запрос GET, генерируем форму для ввода номера документа
        form = DocumentIdentifierForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', data)



def about(request):
    return render(request, 'main/about.html')
