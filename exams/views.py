from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TiposExames

# Create your views here.

@login_required(login_url='/auth/login')
def requestExams(request):
    exams_type = TiposExames.objects.all()
    return render(request, 'request/request.html', {'exams_type' : exams_type})