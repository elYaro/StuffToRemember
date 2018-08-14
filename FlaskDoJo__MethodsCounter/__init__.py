from flask import Flask, render_template, request, redirect
app = Flask(__name__)

counter = {'GET':0, 'POST':0, 'DELETE':0, 'PUT':0}


@app.route('/')
def index():
    global counter
    return render_template('index.html', counter = counter)


@app.route('/request-counter', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def request_counter():
    global counter 
    counter[request.method] +=1
    return redirect('/')
    

@app.route('/statics')
def statics():
    return render_template('statics.html', counter = counter)



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 