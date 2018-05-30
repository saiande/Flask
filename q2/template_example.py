from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    student = {'name': 'Ali', 'address':'Stony Brook Univerity', 'zipcode': '11790'}
    return render_template('student_info.html', title='Student Information Page', student=student)


if __name__ == '__main__':
    app.run()
