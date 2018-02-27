from django.shortcuts import render
from core.models import StatusProcess


def detail(request):
    process_list = StatusProcess.objects.all()
    return render(request, 'list.html', {'processes': process_list})
