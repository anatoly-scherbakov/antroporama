from bottle import route, run, static_file, jinja2_view, Bottle
import jinja2
import os.path
import data

app = application = Bottle()

@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root=os.path.join(
        os.path.dirname(__file__), 'static'
    ))


@app.route('/media/<filepath:path>')
def serve_media(filepath):
    return static_file(filepath, root=os.path.join(
        os.path.dirname(__file__), 'media'
    ))


@app.route('/')
@jinja2_view('index.html', template_lookup=['templates'])
def index():
    return {
        'species': data.species,
        'human_from_clay': data.human_from_clay,
        'reasons': data.reasons,
        'header': data.header,
        'footer': data.footer,
    }


if __name__ == '__main__':
    run(
        app=app,
        host='0.0.0.0',
        port=8000,
        debug=True
    )
