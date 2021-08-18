# from typing_extensions import Required
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from rest_framework.views import APIView
from .serializers import *
from rest_framework import status
from datetime import datetime
from rest_framework.response import Response

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None

class Formdata(APIView):
	"""
	Request Data
	{
		"Billing_name" : "",
		"Billing_Address" : "",
		"Plan_Description" : "",
		"Plan_Cost" : "",
		"Installation":"",
		"Quantity" : "",
		"Invoice_date" : "",
		"Due_date": "",
		"Payment_mode" : "",
		"Paid_date" : "",
		"Paid_amt" : "",
	}
	"""
	def post(self, request):
		try:
			data = request.data
			data["Invoice_date"] = datetime.strptime(data["Invoice_date"],"%Y-%m-%d")
			data["Due_date"] = datetime.strptime(data["Due_date"],"%Y-%m-%d")
			data["Paid_date"] = datetime.strptime(data["Paid_date"],"%Y-%m-%d")
			serializer = FormDSerializer(data=data)
			f_objs =FormD.objects.all()
			if serializer.is_valid(raise_exception=True):
				if f_objs.count():
					f_obj=f_objs.first()
					bn=f_obj.Bill_no
					iid = str(f_obj.Invoice_id)[8:]
					f_obj.delete()
					serializer.save(Invoice_id="Invoice_"+str(int(iid)+1),Bill_no=int(bn)+1,Ref_no="Ref_"+str(uuid.uuid4())[:10],Total=int(data["Quantity"])*int(data["Plan_Cost"]),Grand_total=(int(data["Quantity"])*int(data["Plan_Cost"]))+320+data["Installation"])
				else:	
					serializer.save(Ref_no="Ref_"+str(uuid.uuid4())[:10],Total=int(data["Quantity"])*int(data["Plan_Cost"]),Grand_total=(int(data["Quantity"])*int(data["Plan_Cost"]))+320+data["Installation"])
				return Response(data=serializer.data, status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	
class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('app/pdf_template.html', {'formdata':FormD.objects.first()})
		return HttpResponse(pdf, content_type='application/pdf')

class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('app/pdf_template.html', {'formdata':FormD.objects.first()})
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "{}.pdf".format(FormD.objects.first().Invoice_id)
		content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response

def index(request):
	context = {}
	return render(request, 'app/index.html', context)