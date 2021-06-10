from django.db import models
import uuid
# Create your models here.
class FormD(models.Model):
    Billing_name = models.CharField(max_length=100, null=True, blank=True)
    Billing_Address = models.CharField(max_length=500, null=True, blank=True)
    Plan_Description = models.CharField(max_length=1000, null=True, blank=True)
    Plan_Cost = models.CharField(max_length=100, null=True, blank=True)
    Total = models.CharField(max_length=100, null=True, blank=True)
    Invoice_id = models.UUIDField(primary_key=True, default="inv_"+str(uuid.uuid4)[:10], unique=True)
    Quantity = models.CharField(max_length=100, null=True, blank=True)
    Invoice_date = models.DateTimeField()
    Due_date = models.DateTimeField()