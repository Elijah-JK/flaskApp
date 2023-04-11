from flask import Flask, render_template, request

app = Flask(__name__)

def readDetails(filepath):
    with open(filepath, 'r') as f:
        return [line for line in f]

def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message + '\n')

@app.route("/user/<name>")
def greet(name):
    return f"<p> Hello, {name}! </p>"

@app.route('/form', methods=['GET', 'POST']) 
def formDemo():
    name =  None
    if request.method == 'POST':
        if (request.form['name']):
            name=request.form['name']
        # name = 'Henry'
        elif (request.form['message']):
            writeToFile('static/comments.txt', request.form['message'])
    return render_template('form.html', name=name, aboutMe = [])

@app.route("/")
def homePage():
    name = "Elijah K"
    details = readDetails('static/details.txt')
    # details = ['These are my details', 'This is my background', 'potato']
    return render_template('base.html', name = name, aboutMe  = details)

if __name__ == "__main__":
    app.run(debug = True)
