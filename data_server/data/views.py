from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator

import django_tables2 as tables

from .models import Data
from .tables import SimpleTable

# def dataTable(request):
#   data = Data.objects
#   data_list = Data.objects.all()
#   paginator = Paginator(data_list, 15)
#   page = request.GET.get('page')
#   contents = paginator.get_page(page)

def indexPage(request):
#   data = Data.objects
  data_table = Data.objects.all()
#   # data_table = SimpleTable(Data.objects.all())
#   # data_table.paginate(page = request.GET.get("page", 1), per_page=20)
  return render(request, 'index.html', {"table": data_table})

def popupPage(request):
  return render(request, 'popup.html')


