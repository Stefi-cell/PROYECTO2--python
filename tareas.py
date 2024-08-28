
tareas = {}

def agregar_tarea(tareas, id, descripcion, prioridad):
        """Agrega una nueva tarea con un ID único, descripción y prioridad."""
        if id in tareas:
            raise ValueError(f"Ya existe una tarea con ID {id}")
        tareas[id] = {
            "descripcion": descripcion,
              "prioridad": prioridad,
                "completado": False
                }

def actualizar_tarea(tareas, id, descripcion=None, prioridad=None):
        """Actualiza la descripción y la prioridad de una tarea existente."""
        if id not in tareas:
            raise KeyError(f"No existe una tarea con ID {id}")
        if descripcion is not None:
            tareas[id]["descripcion"] = descripcion
        if prioridad is not None:
            tareas[id]["prioridad"] = prioridad

def marcar_completada(tareas, id):
        """Marca una tarea como completada."""
        if id not in tareas:
            raise KeyError(f"No existe una tarea con ID {id}")
        tareas[id]["completado"] = True

def eliminar_tarea(tareas, id):
        """Elimina una tarea del sistema."""
        if id not in tareas:
            raise KeyError(f"No existe una tarea con ID {id}")
        del tareas[id]

def lista_de_tareas (tarea,tareas, completada=False):
        """Devuelve una lista de tareas pendientes si completada=False, o una lista de tareas completadas si completadas=True."""
        lista_de_tareas = []
        for id, tarea in tareas():
            if tarea["completada"] == completada:
                lista_de_tareas.append({
                    "id": id,
                      "descripcion": tarea["descripcion"],
                        "prioridad": tarea["prioridad"]
                        })
        return lista_de_tareas

