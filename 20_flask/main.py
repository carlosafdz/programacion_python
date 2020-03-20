from flask import Flask

app = Flask('__name__')


@app.route('/')
def holamundo():
    return "Hola mundo"

if __name__ == "__main__":
    app.run()