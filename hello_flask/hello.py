from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-aligned: center">Hello, World 123</h1>' \
    "<p>This is a paragraph </p>"

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


@app.route('/bye')
@make_bold
def bye():
    return 'Hello, bye 123' 

@app.route('/<name>')
def name12(name):
    return f'Hello, bye 123{name + 1}' 



if __name__ == "__main__":
    app.run(debug=True)