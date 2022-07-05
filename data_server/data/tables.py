import django_tables2 as tables

from .models import Data

class SimpleTable(tables.Table):
  class Meta:
    model = Data
    template_name = "index.html"
