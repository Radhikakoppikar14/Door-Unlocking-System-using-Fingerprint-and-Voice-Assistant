from flask import Blueprint, request, jsonify
from models import db, Project, Task, User

api = Blueprint('api', __name__)

@api.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    new_project = Project(name=data['name'], description=data.get('description', ''))
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Project created successfully!'})

@api.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    output = []
    for project in projects:
        project_data = {}
        project_data['id'] = project.id
        project_data['name'] = project.name
        project_data['description'] = project.description
        output.append(project_data)
    return jsonify({'projects': output})

@api.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.get_json()
    project.name = data['name']
    project.description = data.get('description', '')
    db.session.commit()
    return jsonify({'message': 'Project updated successfully!'})

@api.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Project deleted successfully!'})

@api.route('/projects/<int:project_id>/tasks', methods=['POST'])
def create_task(project_id):
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description', ''), project_id=project_id)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully!'})

@api.route('/projects/<int:project_id>/tasks', methods=['GET'])
def get_tasks(project_id):
    tasks = Task.query.filter_by(project_id=project_id).all()
    output = []
    for task in tasks:
        task_data = {}
        task_data['id'] = task.id
        task_data['title'] = task.title
        task_data['description'] = task.description
        task_data['status'] = task.status
        output.append(task_data)
    return jsonify({'tasks': output})

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)
    db.session.commit()
    return jsonify({'message': 'Task updated successfully!'})

@api.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'})

@api.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['username'] = user.username
        user_data['email'] = user.email
        user_data['role'] = user.role
        output.append(user_data)
    return jsonify({'users': output})

@api.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.username = data.get('username', user.username)
    user.email = data.get('email', user.email)
    user.role = data.get('role', user.role)
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})

@api.route('/projects/<int:project_id>/assign', methods=['POST'])
def assign_user_to_project(project_id):
    data = request.get_json()
    user_id = data['user_id']
    project = Project.query.get_or_404(project_id)
    user = User.query.get_or_404(user_id)
    project.team_members.append(user)
    db.session.commit()
    return jsonify({'message': f'User {user.username} assigned to project {project.name} successfully!'})

@api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})

@api.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully!'})
