from django.shortcuts import render
from .models import Prpdutos

def index(request):

    #print(dir(request.user))
    #print(f'Usuario:{request.user}')
    #print(request.user.last_name)
    #print(request.user.email_user)
    produtos = Prpdutos.objects.all()

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuario não logado'
    else:
        teste = 'Usuario logado'
        print(request.user)


    text = {'projeto':'funcao index ',
            'logado':teste,
             'produtos':produtos}
    return render(request,'index.html',text)

def contados(request,pk):
    
    prod = Prpdutos.objects.get(id=pk)
    context = {'produto':prod}
    return render(request,'contados.html',context)

    
