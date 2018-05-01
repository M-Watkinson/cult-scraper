from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from cultlistings import cult_data

app = Flask(__name__)

app.config['DEBUG'] = True

app.config['SECRET_KEY'] = 'c0ND3N4Mbp'

Bootstrap(app)

def get_cult(source, id):
    for row in source:
        if id == str( row["id"] ):
            cult = row["cult"]
            founder = row["founder"]
            year_founded = row["year founded"]
            type = row["type"]
            id = str(id)
            return id, cult, founder, year_founded, type

@app.route('/')
def index():
    ids_list = []
    name_list = []
    for cult in cult_data:
        ids_list.append(cult['id'])
        name_list.append(cult['cult'])
    pairs_list = zip(ids_list, name_list)
    return render_template('index.html', pairs=pairs_list, the_title=("New Religious Movements and Cults"))

@app.route('/cult/<id>.html')
def cult(id):
    id, cult, founder, year_founded, type = get_char(character_data, id)
    return render_template('cult.html', cult=cult, founder=founder, year_founded=year_founded, type=type)

if __name__ == '__main__':
    app.run(debug=True)
