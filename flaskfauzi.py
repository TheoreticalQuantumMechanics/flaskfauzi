from flask import Flask, render_template
app = Flask(__name__)
# @app.route('/')
# def hello():
#     #html file
#     return "hello world, and congratulations fauzi"

@app.route('/index')
def index():
    # html file
    return render_template('index.html')

if __name__== '__main__':
    app.run()