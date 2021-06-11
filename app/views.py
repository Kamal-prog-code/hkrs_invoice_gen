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
		"Total" : "",
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
			serializer = FormDSerializer(data=data)
			f_objs =FormD.objects.all()
			if serializer.is_valid(raise_exception=True):
				if f_objs.count():
					f_obj=f_objs.first()
					bn=f_obj.Bill_no
					iid = str(f_obj.Invoice_id)[4:]
					rn=str(f_obj.Ref_no)[4:]
					f_obj.delete()
					serializer.save(Invoice_id="inv_"+str(int(iid)+1),Bill_no=int(bn)+1,Ref_no="Ref_"+str(int(rn)+1))
				else:	
					serializer.save(Invoice_id="inv_1",Bill_no=155110,Ref_no="Ref_1")
				return Response(data=serializer.data, status=status.HTTP_201_CREATED)
		except Exception as e:
			return Response({'message':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	

#Opens up page as PDF
class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('app/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		
		pdf = render_to_pdf('app/pdf_template.html', data)

		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename=%s" %(filename)
		response['Content-Disposition'] = content
		return response



def index(request):
	context = {}
	return render(request, 'app/index.html', context)