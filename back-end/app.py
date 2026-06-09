from flask import Flask, jsonify, request
# from flask_sqlalchemy import 


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Study Python',
        'description': 'Create an API with Python'
    },
    {
        'id': 2,
        'title': 'Read API documentation',
        'description': 'Learn parameters from API'
    },
    {
        'id': 3,
        'title': 'Study Javascript Asynchronous',
        'description': 'Learn async, await and fetch'
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for task in tasks:
        if task.get('id') == id:
            return jsonify(task)

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task_by_id(id):
    updated_task = request.get_json()
    for index, task in enumerate(tasks):
        if task.get('id') == id:
            tasks[index].update(updated_task)
            return jsonify(tasks[index])

@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    tasks.append(new_task)
    return jsonify(tasks)

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task_by_id(id):
    for index, task in enumerate(tasks):
        if task.get('id') == id:
            del tasks[index]
            return jsonify(tasks)


app.run(port=5000, host='localhost', debug=True)
