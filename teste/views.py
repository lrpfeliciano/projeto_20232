from django.shortcuts import redirect, render
from django.http import HttpResponse
from teste.forms import AlunoForm

from teste.models import Aluno

# Create your views here.
def index(request):
    return HttpResponse("Olá, Mundo! Agora é na Web.")

def novo(request):
    return HttpResponse("Isso é uma requisição")

def listarAluno(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_aluno.html', 
                  {'alunos': alunos})

def incluirAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'incluir_aluno.html', 
                  {'form': form})

def editarAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(instance=aluno)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')

    return render(request, 'incluir_aluno.html',
                  {'form': form})


def excluirAluno(request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('listar_alunos')


def listarCurso(request):
    pass