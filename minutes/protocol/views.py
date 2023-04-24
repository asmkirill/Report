from django.shortcuts import render
from django.http import JsonResponse
from .forms import ProtocolDataForm
from .models import ProtocolData


def create_protocol(request):
    if request.method == 'POST':
        form = ProtocolDataForm(request.POST)
        if form.is_valid():
            # Create and save new records in the database
            protocol = form.save(commit=False)
            # Get the list of protocol items from the form data
            items = request.POST.getlist('item[]')
            responsibles = request.POST.getlist('responsible[]')
            deadlines = request.POST.getlist('deadline[]')
            statuses = request.POST.getlist('status[]')
            # Loop through the list of items and create ProtocolData objects
            for i in range(len(items)):
                protocol_item = ProtocolData(
                    title=form.cleaned_data['title'],
                    no=form.cleaned_data['no'],
                    item=items[i],
                    responsible=responsibles[i],
                    deadline=deadlines[i],
                    status=statuses[i],
                    notes=form.cleaned_data['notes']
                )
                protocol_item.save()
            # Save all created objects to the database
            protocol.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProtocolDataForm()
    return render(request, 'protocol/create_protocol.html', {'form': form})










# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .forms import ProtocolDataForm
#
#
# @csrf_exempt
# def create_protocol(request):
#     form = ProtocolDataForm(request.POST or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             if request.is_ajax():
#                 return JsonResponse({'success': True})
#             else:
#                 return redirect('index')
#         else:
#             if request.is_ajax():
#                 return JsonResponse({'success': False, 'errors': form.errors})
#             else:
#                 data = {
#                     'form': form,
#                     'csrf_token': request.COOKIES.get('csrftoken')
#                 }
#                 return render(request, 'protocol/create_protocol.html', data)
#     else:
#         data = {
#             'form': form,
#             'csrf_token': request.COOKIES.get('csrftoken')
#         }
#         return render(request, 'protocol/create_protocol.html', data)
#
