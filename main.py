from flask import Flask, escape, request, render_template  # @iLevanta
from classes import Deck

app = Flask(__name__)
deck = Deck()

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
        text = request.form.get("text")
        rev1 = text[::-1]  # slice
        rev2 = "".join(list(reversed(text)))  # reversed
        rev3 = "".join([x for x in reversed(text)])  # comprehension
        return f'{rev1},{rev2},{rev3}'

@app.route('/third', methods=['GET','POST'])
def third():
    if request.method == 'GET':
        return render_template('third.html', content='\u0020', deck=str(deck))
    else:
        if "shuffle" in request.form:
            deck.shuffle()
            value = "Deck was shuffled"
        elif "pop" in request.form:
            value = deck.pop()
        elif "get_random" in request.form:
            value = deck.get_random()
        else:
            num = request.form.get("index")
            value = deck.index(num)
        return render_template('third.html', content=value)
if __name__ == '__main__':
    app.run('0.0.0.0')
