from django.db import models
import django_tables2 as tables

# Create your models here.
class Data(models.Model):
    # def __init__(self, __id, __status, __business_category, __company, __created_date, __modified_date):
    #     self.id = __id
    #     self.status = __status
    #     self.business_category = __business_category
    #     self.company = __company
    #     self.created_date = __created_date
    #     self.modified_date = __modified_date
  # def __repr__(self):
  #     # return '<Data: {"id": "'+self.id+'", "status": "'+self.status+'", "business_category": "'+self.business_category+'", "company": "'+self.company+'", "created_date": "'+self.created_date+'", "modified_date": "'+self.modified_date+'"}>'
  #     return '{"id": "'+self.id+'", "status": "'+self.status+'", "business_category": "'+self.business_category+'", "company": "'+self.company+'", "created_date": "'+self.created_date+'", "modified_date": "'+self.modified_date+'"}'
  #     # data_dict = {"id": self.id, "status": self.status, "business_category": self.business_category, "company": self.company, "created_date": self.created_date, "modified_date": self.modified_date}

  # def __str__(self):
  #     # return '<Data: {"id": '+self.id+', "status": "'+self.status+'", "business_category": "'+self.business_category+'", "company": "'+self.company+'", "created_date": "'+self.created_date+'", "modified_date": "'+self.modified_date+'"}>'
  #     return '{"id": "'+self.id+'", "status": "'+self.status+'", "business_category": "'+self.business_category+'", "company": "'+self.company+'", "created_date": "'+self.created_date+'", "modified_date": "'+self.modified_date+'"}'
  #     # return {"id": self.id, "status": self.status, "business_category": self.business_category, "company": self.company, "created_date": self.created_date, "modified_date": self.modified_date}

  ACTIVE = 'ACTIVE'
  INACTIVE = 'INACTIVE'
  STATUS_CHOICE = [
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
  ]
  id = models.BigAutoField(primary_key=True)
  status = models.CharField(max_length=10, default=INACTIVE, choices=STATUS_CHOICE)
  business_category = models.CharField(max_length=30)
  company = models.CharField(max_length=15)
  created_date = models.DateTimeField(auto_now_add=True)
  modified_date = models.DateTimeField(null=True)

