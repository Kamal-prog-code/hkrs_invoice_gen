from django.db import models
import uuid
# Create your models here.
class FormD(models.Model):
    Billing_name = models.CharField(max_length=100, null=True, blank=True)
    Billing_Address = models.CharField(max_length=500, null=True, blank=True)
    Plan_Description = models.CharField(max_length=1000, null=True, blank=True)
    Plan_Cost = models.CharField(max_length=100, null=True, blank=True)
    Total = models.CharField(max_length=100, null=True, blank=True)
    Invoice_id = models.UUIDField(primary_key=True, default="inv_"+str(uuid.uuid4())[:10], unique=True)
    Quantity = models.CharField(max_length=100, null=True, blank=True,default=1)
    Invoice_date = models.DateTimeField()
    Due_date = models.DateTimeField()
    Payment_mode = models.CharField(max_length=500, null=True, blank=True)
    Bill_no = models.CharField(max_length=1000, null=True, blank=True)
    Ref_no = models.CharField(max_length=1000, null=True, blank=True)
    Paid_date = models.DateTimeField()
    Paid_amt = models.CharField(max_length=100, null=True, blank=True)

class BillNo(models.Model):
    Bill_no = models.CharField(max_length=1000, null=True, blank=True)
    Ref_no = models.CharField(max_length=1000, null=True, blank=True,default="Ref_"+str(uuid.uuid1().int)[:1])
    
    def __str__(self):
        return self.Bill_no