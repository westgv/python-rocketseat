import pytest
import requests 

# CRUD
BASE_URL = 'http://localhost:5000'
tasks =[]

def test_create_task():
    new_task_data = {
        "title" : "Nova Tarefa",
        "Description" : "Descrição da nova tarefa",
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id']) 

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    assert "tasks" in response.json()
    assert "total_tasks" in response.json()

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['id'] == task_id

def test_update_task():
    if tasks:
        tasks_id = tasks[0]
        updated_data = {
            "title": "Tarefa Atualizada",
            "description": "Descrição atualizada",
            "completed": True
        }
        response = requests.put(f"{BASE_URL}/tasks/{tasks_id}", json=updated_data)
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['message'] == "Tarefa atualizada com sucesso"


        # Nova requisição para verificar se a tarefa foi atualizada
        response = requests.get(f"{BASE_URL}/tasks/{tasks_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['title'] == updated_data['title']
        assert response_json['description'] == updated_data['description']
        assert response_json['completed'] == updated_data['completed']

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['message'] == "Tarefa excluída com sucesso"

        # Verificar se a tarefa foi realmente excluída
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404