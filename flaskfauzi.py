from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    #html file
    return "hello world, and congratulations fauzi"

@app.route('/about')
def about():
    # html file
    return "about me"

if __name__== '__main__':
    app.run()