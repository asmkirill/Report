from django.utils import timezone
from .models import ProtocolData
from .forms import ProtocolDataForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ProtocolDataForm


@csrf_exempt
def create_protocol(request):
    form = ProtocolDataForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return JsonResponse({'success': True})
            else:
                return redirect('index')
        else:
            if request.is_ajax():
                return JsonResponse({'success': False, 'errors': form.errors})
            else:
                data = {
                    'form': form,
                    'csrf_token': request.COOKIES.get('csrftoken')
                }
                return render(request, 'protocol/create_protocol.html', data)
    else:
        data = {
            'form': form,
            'csrf_token': request.COOKIES.get('csrftoken')
        }
        return render(request, 'protocol/create_protocol.html', data)




# def create_protocol(request):
#     form = ProtocolDataForm()
#     if request.method == 'POST':
#         form = ProtocolDataForm(request.POST)
#         if form.is_valid():
#             protocol = form.save(commit=False)
#             protocol.save()
#             return redirect('index')
#     data = {
#         'form': form,
# #        'protocol_id': protocol_id,
#     }
#     return render(request, 'protocol/create_protocol.html', data)
