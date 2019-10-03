from flask import Blueprint, request, jsonify

teacher_db = []
teacher_app = Blueprint('teacher_app', __name__)

@teacher_app.route('/professores')
def get_all_teachers():
    return jsonify(teacher_db)

@teacher_app.route('/professores', methods=["POST"])
def store_teacher():
    new_teacher = request.json
    if not 'nome' in new_teacher.keys():
        return jsonify({ 'erro': 'professor sem nome' }), 404

    for teacher in teacher_db:
        if teacher['id'] == new_teacher['id']:
            return jsonify({ 'erro': 'id já utilizada' }), 404

    teacher_db.append(new_teacher)
    return jsonify({ 'success': True }), 200

@teacher_app.route('/professores/<int:id_teacher>')
def get_single_teacher(id_teacher):
    for teacher in teacher_db:
        if teacher['id'] == id_teacher:
            return teacher

    return jsonify({ 'erro': 'professor não encontrado' }), 404

@teacher_app.route('/professores/<int:id_teacher>', methods=["DELETE"])
def del_teacher(id_teacher):
    for teacher in teacher_db:
        if teacher['id'] == id_teacher:
            teacher_db.remove(teacher)
            return jsonify({ 'success': True })

    return jsonify({ 'erro': 'professor não encontrado' }), 404

@teacher_app.route('/professores/<int:id_teacher>', methods=["PUT"])
def change_teacher(id_teacher):
    if not 'nome' in request.json.keys():
        return jsonify({ 'erro': 'professor sem nome' }), 404

    for teacher in teacher_db:
        if teacher['id'] == id_teacher:
            teacher['nome'] = request.json['nome']
            return jsonify({ 'success': True })

    return jsonify({ 'erro': 'professor não encontrado' }), 404

def reset_teacher():
    teacher_db = []