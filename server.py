from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/ninjas')
# def ninjas():
#     return render_template('ninjas.html')

# @app.route('/dojo')
# def dojo():
#     return render_template('dojo.html')

@app.route('/process', methods=['POST'])
def process():
    print('Welcome Ninja')
    name = request.form['name']
    return render_template('ninjas.html', name = name)
if __name__=="__main__":
    app.run(debug = True)