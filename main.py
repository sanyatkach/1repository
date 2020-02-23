from flask import Flask, escape, request #@iLevanta

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Oleksandr Tkachenko TS-91'
@app.route('/first')
def first():
    n = None
    num = 12
    str = '213'
    return f'{escape(n)}:{escape(num)},{escape(str)}'
if __name__ == '__main__':
    app.run('0.0.0.0')
