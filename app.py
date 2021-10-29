from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def import_json():
    with open('./recipes.json') as f:
        return json.load(f)

def dump_json(injson):
    with open('./recipes.json', 'w') as f:
        json.dump(injson, f)


@app.route('/clear', methods=['POST'])
def clear():
    if request.method == 'POST':
        f=request.json
        if f['key'] == ";F05lUCw%[hUeD?84~XMK{E@OO}4uPdYB4do'?8bH-BlSTuh9#|W=TzS(Pq9e":
            dump_json({'recipes': []})
            return 'done'
        else:
            return 'invalid key'


@app.route('/upload', methods=['POST'])
def add_recipe():
    if request.method == 'POST':
        # f = request.files['file']
        # f.save(secure_filename(f.filename))
        f= request.json
        print(f['name'])

        todump = import_json()
        todump['recipes'].append(f)
        dump_json(todump)

        return todump


if __name__ == '__main__':
    app.run(debug=True)
