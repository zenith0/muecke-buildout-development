# Create your views here.
from django.shortcuts import render_to_response

from django.utils.log import getLogger
logger = getLogger('ecomstore')

def home(request):
    return render_to_response("index.html", locals())