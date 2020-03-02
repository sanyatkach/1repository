from flask import Flask, escape, request, render_template  # @iLevanta

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
@app.route('/second', methods=['GET','POST'])
def second():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        text = request.form.get('text')
        first = "".join(reversed(text))
        return render_template('index.html', first=first)
        # you can add text on this page again without reloading it
if __name__ == '__main__':
    app.run('0.0.0.0')
