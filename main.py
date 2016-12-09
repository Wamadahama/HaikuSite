from flask import Flask, request, session,g, redirect, url_for, abort, render_template, flash

from lib import generator

app = Flask(__name__)

@app.route("/")
def render_haiku():
    haiku_generator = generator.Generator(corpus_directory='lib/res/corpus_texts/')
    return render_template('index.html', haiku=haiku_generator.generate_haiku())

@app.route("/haiku", methods=['POST'])
def new_haiku():
    corpus = request.form['input-haiku']
    haiku_generator = generator.Generator(text=corpus)
    return render_template('index.html', haiku=haiku_generator.generate_haiku())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True, port=5001)
