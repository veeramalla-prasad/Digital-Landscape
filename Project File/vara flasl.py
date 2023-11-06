from flask import Flask, render_template, request


digital = Flask(__name__) # initializng the flask app


@digital.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == '__main__':
    digital.run(debug = False, port = 5000)