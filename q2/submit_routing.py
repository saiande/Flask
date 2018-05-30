from flask import Flask, render_template, redirect, url_for
from text_form import SubmissionForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'


@app.route('/', methods=['GET', 'POST'])
def login():
    form = SubmissionForm()
    global numOne
    global numTwo
    global op
    if form.validate_on_submit():
        numOne = form.first.data
        numTwo = form.second.data
        op = form.operation.data
        if((type(numOne) != int and type(numOne) != float) or (type(numTwo) != int and type(numTwo) != float)):
            return redirect(url_for('error'))
        elif(op == "add"):
        	return redirect(url_for('add'))
        elif(op == "subtract"):
        	return redirect(url_for('subtract'))
        elif(op == "multiply"):
        	return redirect(url_for('multiply'))
        elif(op == "divide"):
        	return redirect(url_for('divide'))
    return render_template('submit.html', title='Submit', form=form)

@app.route('/result/error')
def error():
    return render_template('error.html', title='Error')

@app.route('/result/add')
def add():
    answer = (numOne+numTwo)
    return render_template('result.html', title='Answer', answer=answer)

@app.route('/result/subtract')
def subtract():
    answer = (numOne-numTwo)
    return render_template('result.html', title='Answer', answer=answer)

@app.route('/result/multiply')
def multiply():
    answer = (numOne*numTwo)
    return render_template('result.html', title='Answer', answer=answer)

@app.route('/result/divide')
def divide():
    answer = (numOne/numTwo)
    return render_template('result.html', title='Answer', answer=answer)

@app.errorhandler(403)
def forbidden(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    # db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run()
