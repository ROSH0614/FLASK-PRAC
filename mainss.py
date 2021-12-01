from flask import Flask,redirect,render_template,url_for,request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('indexx.html')


@app.route('/success/<int:score>')
def success(score):
    res=" "
    if score>=50:
        res="pass"
    else:
        res="failed"
    return render_template('result.html',result=res)

@app.route('/failure/<int:score>')
def failure(score):
    return "the person has failed and the score is" +str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result = 'failure'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))

###result checker html 

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score =0
    if request.method=='POST':
        science =float(request.form['science'])
        maths = float(request.form['maths'])
        social =float(request.form['social'])
        data_science=float(request.form['data_science'])
        total_score=(science+maths+social+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))
    

if __name__ == "__main__":
    app.run(debug=True)

