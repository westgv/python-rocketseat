from flask import Flask, request, jsonify
from task import Task

app = Flask(__name__)

#CRUD: CREATE READ UPDATE DELETE
# Tabela: Tarefa

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control,title=data['title'],description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"mensagem" : "Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks" : len(task_list)
    }

    print(output)
    return jsonify(output)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for t in tasks:
        if t.id == task_id:
            return jsonify(t.to_dict())
    return jsonify({"mensagem": "Tarefa não encontrada"}), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
  task = None
  for t in tasks:
    if t.id == id:
      task = t
      break
  if task == None:
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

  data = request.get_json()
  task.title = data['title']
  task.description = data['description']
  task.completed = data['completed']
  return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if not task:
        return jsonify({"message": "Tarefa não encontrada"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True) 