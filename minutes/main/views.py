from django.shortcuts import render, redirect
from .forms import DocumentIdentifierForm
from .models import DocumentsIdentifier


def index(request):
    error = ''
    if request.method == 'POST':
        form = DocumentIdentifierForm(request.POST)
        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            try:
                documents_identifier = DocumentsIdentifier.objects.get(identifier=identifier)
            except DocumentsIdentifier.DoesNotExist:
                error = 'Document not found'
            else:
                return redirect('create_protocol', id=documents_identifier.id)
        else:
            error = 'Document not found'
    else:
        form = DocumentIdentifierForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/index.html', data)



def about(request):
    return render(request, 'main/about.html')
