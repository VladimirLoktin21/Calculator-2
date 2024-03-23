from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def check_answers(answer1, answer2, answer3):
    correct_answer1 = "ExtremeWeather"
    correct_answer2 = "ReducingEmissions"
    correct_answer3 = "CO2"

    score = 0
    if answer1 == correct_answer1:
        score += 1
    if answer2 == correct_answer2:
        score += 1
    if answer3 == correct_answer3:
        score += 1

    return score

@app.route('/')
def index():
    return render_template('global_warming_questions.html')

@app.route('/quiz')
def question1():
        return render_template('question1.html')

@app.route('/quiz/<answer1>')
def question2(answer1):
        return render_template('question2.html', 
                               answer1=answer1)

@app.route('/quiz/<answer1>/<answer2>')
def question3(answer1, answer2):
        return render_template('question3.html',
                               answer1=answer1,
                               answer2=answer2)


@app.route('/quiz/<answer1>/<answer2>/<answer3>')
def show_result(answer1, answer2, answer3):
    score = check_answers(answer1, answer2, answer3)
    return render_template('quiz_result.html', score=score)

@app.route('/finish')
def finish_quiz():
    return redirect(url_for('show_result', answer1=request.args.get('answer1'), answer2=request.args.get('answer2'), answer3=request.args.get('answer3')))

if __name__ == '__main__':
    app.run(debug=True)
