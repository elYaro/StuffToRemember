from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def index():
    data = request.get_json(force=True)
    name = data['name']
    location = data['location']
    samplelist = data['samplelist']
    return jsonify({'name':name, 'location' : location, 'samplelist' : samplelist[1]})




if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 