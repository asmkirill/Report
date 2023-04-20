from django.shortcuts import render, redirect
from django.utils.timezone import now
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




# def index(request):
#     error = ''
#     if request.method == 'POST':
#         form = DocumentIdentifierForm(request.POST)
#         if form.is_valid():
#             identifier = form.cleaned_data['identifier']
#             try:
#                 documents_identifier = DocumentsIdentifier.objects.get(identifier=identifier)
#             except DocumentsIdentifier.DoesNotExist:
#                 error = 'Document not found'
#             else:
#                 pass
#         else:
#             error = 'Document not found'
#     else:
#         form = DocumentIdentifierForm()
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main/index.html', data)


# def create_protocol(request):
#     # Generate unique identifier for the new document
#     last_document = DocumentsIdentifier.objects.last()
#     if last_document:
#         last_id = int(last_document.identifier.split('.')[1])
#     else:
#         last_id = 0
#     new_id = f"{now().strftime('%Y%m%d')}.{str(last_id + 1).zfill(4)}"
#
#     # Create new document object
#     document = DocumentsIdentifier.objects.create(identifier=new_id, title='New Protocol')
#
#     # Redirect to the create protocol page for the new document
#     return redirect('create_protocol', id=document.id)



# from django.shortcuts import render, redirect
# from .forms import DocumentIdentifierForm
# from .models import DocumentsIdentifier

#




def about(request):
    return render(request, 'main/about.html')
