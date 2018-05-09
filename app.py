from flask import Flask, render_template, request, jsonify
from gevent.wsgi import WSGIServer

from colemankb.annotations import ColemanKB

app = Flask(__name__)
app.debug = True

s = ColemanKB()


@app.route("/")
def main():
    s.connect_spreadsheet()
    return 'Hello'


@app.route("/annotate")
def annotate():

    s.protein_change = request.args.get('protein_change')
    s.variant_type = request.args.get('variant_type')
    s.gene = request.args.get('gene')
    try:
        s.exac = float(request.args.get('exac'))
    except TypeError:
        s.exac = ''

    tier = s.annotate_variant()

    data = {
        'gene': s.gene,
        'protein_change': s.protein_change,
        'variant_type': s.variant_type,
        'tier': tier,
    }
    return jsonify(data)


if __name__ == "__main__":
    http_server = WSGIServer(('0.0.0.0', 4848), app)
    http_server.serve_forever()
    #app.run(host='0.0.0.0',debug=True, port=4848)
