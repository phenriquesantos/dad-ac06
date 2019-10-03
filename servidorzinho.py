from flask import Flask, jsonify, request
import student
import teacher
import subject

app = Flask(__name__)

# @app.route('/')
# def get_all():
#     return jsonify([student_db, student_app]), 200

@app.route('/reseta', methods=["POST"])
def reset():
    student.student_db = []
    teacher.teacher_db = []
    subject.subject_db = []
    return jsonify({ 'success': True }), 200


app.register_blueprint(student.student_app)
app.register_blueprint(teacher.teacher_app)
app.register_blueprint(subject.subject_app)

if __name__ == '__main__':
    app.run(port=5002, debug=True)
