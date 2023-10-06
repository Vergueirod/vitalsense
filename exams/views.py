from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import TiposExames, PedidosExames, SolicitacaoExame
from datetime import datetime

# Create your views here.

@login_required(login_url='/auth/login')
def requestExams(request):
    exams_type = TiposExames.objects.all()

    if request.method == 'GET':
        return render(request, 'request/request.html', {'exams_type' : exams_type})
    elif request.method == 'POST':
            opt_exams = request.POST.getlist('exams') # Pega os dados do usuario
            request_exams = TiposExames.objects.filter(id__in=opt_exams) # consulta os dados no banco
            valitation = TiposExames.objects.filter(id__in=opt_exams, disponivel=True)
            
            preco_total = 0
            for i in valitation: # realiza a query
                 preco_total +=  i.preco

            return render(request, 'request/request.html', {'exams_type' : exams_type, # Libera os dados para o front consumir
                                                            'request_exams': request_exams,
                                                            'preco_total': preco_total ,})

@login_required(login_url='/auth/login')    
def closeOrders(request):
        
        exams_id = request.POST.getlist('exams')
        request_exams = TiposExames.objects.filter(id__in=exams_id)

        exams_orders = PedidosExames(
            usuario = request.user,
            data = datetime.now()
        )

        exams_orders.save()

        for exams in request_exams:
            request_exams_temp = SolicitacaoExame(
                usuario=request.user,
                exame=exams,
                status="E"
            )
            request_exams_temp.save()
            exams_orders.exames.add(request_exams_temp)
            
        exams_orders.save()

        return redirect('/exams/see_order/')