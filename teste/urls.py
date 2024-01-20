from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('outro', views.novo, name='novo'),

    #Alunos
    path('listar_alunos', views.listarAluno, 
         name='listar_alunos'),
    path('incluir_aluno', views.incluirAluno, 
         name='incluir_aluno'),
    
    path('editar_aluno/<int:id>', views.editarAluno,
         name='editar_aluno'),

    path('excluir_aluno/<int:id>', views.excluirAluno,
         name='excluir_aluno'),

    #Cursos
    #path('')
]