from flask import request, Blueprint, jsonify
from validacao import validar_campos
subject_db = []
subject_app = Blueprint('subject_app', __name__)

@subject_app.route('/disciplinass')
def get_all_subject():
    return jsonify(subject_db), 200

@subject_app.route('/disciplinas', methods=['POST'])
def store_subject():
    validate_data = { 'id': int, 'nome': str, 'status': int, 'plano_ensino': str, 'carga_horaria': int }
    new_subject = request.json
    if validar_campos(new_subject, validate_data):
        return jsonify({ 'erro': True }), 404

    for subject in subject_db:
        if subject['id'] == new_subject['id']:
            return jsonify({ 'erro': 'id já utilizada' }), 404

    subject_db.append(request.json)
    return jsonify({ 'success': True }), 200

@subject_app.route('/disciplinas/<int:subject_id>')
def get_single_subect(subject_id):
    for subject in subject_db:
        if subject_id == subject['id']:
            return jsonify(subject), 200

    return jsonify({ 'erro': 'disciplina não encontrada' }), 404

@subject_app.route('/disciplinas/<int:subject_id>', methods=['DELETE'])
def del_subject(subject_id):
    for subject in subject_db:
        if subject_id == subject['id']:
            subject_db.remove(subject)
            return jsonify({'success': True}), 200

    return jsonify({ 'erro': 'disciplina não encontrada' }), 404


@subject_app.route('/disciplinas/<int:subject_id>')
def change_subject(subject_id):
    validate_data = { 'id': int, 'nome': str, 'status': int, 'plano_ensino': str, 'carga_horaria': int }
    new_subject = request.json
    if validar_campos(new_subject, validate_data):
        return jsonify({ 'erro': True }), 404

    for subject in subject_db:
        if subject['id'] == subject_id:
            subject = request.json
            
            return jsonify({ 'success': True })

    return jsonify({ 'erro': 'disciplina não encontrada' }), 404

    
