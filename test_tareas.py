import pytest
from tareas import agregar_tarea, actualizar_tarea, marcar_completada, eliminar_tarea, lista_de_tareas, tareas

def setup_function():
       tareas.clear()



def test_agregar_tarea ():
        agregar_tarea(1, "Tarea 1", "alta")
        print (len(tareas))
      

def test_actualizar_tarea():
        agregar_tarea(1, "Tarea 1", "alta")
        actualizar_tarea(1, "Tarea 1","media")

        with  pytest.raises(ValueError):
           actualizar_tarea (1, "Tarea 2", "baja")

def test_marcar_completada():
        agregar_tarea (1, "Tarea 1", "alta")
        marcar_completada(1)
        if 1 in tareas:
              True (tareas["completada"])

        with pytest.raises(KeyError):
           marcar_completada(999)

def test_eliminar_tarea():
        agregar_tarea(1, "Tarea 1", "alta")
        eliminar_tarea(1)
        print (len(tareas))

        with pytest.Raises(KeyError):
           eliminar_tarea(999)

def test_lista_de_tareas():
        agregar_tarea(1, "Tarea 1", "alta")
        agregar_tarea(2, "Tarea 2", "media")
        marcar_completada(1)
        
        tarea_pendiente = lista_de_tareas(completed=False)
        tarea_completada = lista_de_tareas(completed=True)

        print(len(pending_tasks), 1)
        print(len(completed_tasks), 1)

