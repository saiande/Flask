from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<studentname>')
def index(studentname):
    ali_info = {'name': 'Ali', 'address':'Stony Brook Univerity', 'zipcode': '11790'}
    trung_info = {'name': 'Trung', 'address':'White House', 'zipcode': '12345'}
    zhibo_info = {'name': 'Zhibo', 'address':'Bloomberg Tower', 'zipcode': '54321'}
    student_info_dict = {'ali': ali_info, 'trung': trung_info, 'zhibo': zhibo_info}
    return render_template('student_info.html', title='Student Information Page', student=student_info_dict[studentname])


if __name__ == '__main__':
    app.run()
