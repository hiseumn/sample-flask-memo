from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if(request.method == 'POST'):
        exampleFormControlTextarea1= request.form.get('exampleFormControlTextarea1')
        return render_template('index.html', exampleFormControlTextarea1=exampleFormControlTextarea1)
    return render_template('index.html')

@app.route("/add")
def add():
    return render_template('index.html')
    
print("add")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
