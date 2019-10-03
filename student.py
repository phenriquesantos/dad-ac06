from flask import Blueprint, request, jsonify

student_db = []

student_app = Blueprint('student_app', __name__)

@student_app.route('/alunos')
def get_all_student():
    return jsonify(student_db)

@student_app.route('/alunos', methods=["POST"])
def store_student():
    if not 'nome' in request.json.keys():
        return jsonify({ 'erro':'aluno sem nome' }), 404

    new_student = request.json
    for student in student_db:
        if student['id'] == new_student['id']:
            return jsonify({ 'erro':'id já utilizada' }), 404
    
    student_db.append(new_student)
    return { 'success': True }, 200

@student_app.route('/alunos/<int:id_student>')
def get_single_stundent(id_student):
    for student in student_db:
        if student['id'] == id_student:
            return jsonify(student)

    return jsonify({ 'erro': 'aluno não encontrado' }), 404

@student_app.route('/alunos/<int:id_student>', methods=["DELETE"])
def del_student(id_student):
    for student in student_db:
        if student['id'] == id_student:
            student_db.remove(student)
            return jsonify({ 'success': True }), 200

    return jsonify({ 'erro': 'aluno não encontrado' }), 404

@student_app.route('/alunos/<int:id_student>', methods=["PUT"])
def change_student(id_student):
    if 'nome' not in request.json.keys():
        return jsonify({ 'erro':'aluno sem nome' }), 404

    for student in student_db:
        if student['id'] == id_student:
            student['nome'] = request.json['nome']
            return jsonify({ 'success': True }), 200

    return jsonify({ 'erro': 'aluno não encontrado' }), 404


def reset_student():
    student_db = []