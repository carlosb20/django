from django.shortcuts import render

def index(request):
    text = {'projeto':'funcao index '}

    return render(request,'index.html',text)

def contado(request):
    return render(request,'contato.html')

    
