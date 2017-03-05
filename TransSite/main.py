from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

lang_mapping = {
    'ua': 'ukrainian.json',
    'en': 'english.json'
}

@app.route("/<lang>")
def index(lang):
    with open('translations/' + lang_mapping[lang], encoding="utf8") as trans_file:
        data = json.load(trans_file)

    return render_template('index.html', **data)

if __name__  == "__main__":
    app.run()
