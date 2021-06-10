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
	def post(self, request):
		try:
			data = request.data
			serializer = FormDSerializer(data=data)
			if serializer.is_valid(raise_exception=True):
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