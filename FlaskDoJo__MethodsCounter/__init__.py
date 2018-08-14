from flask import Flask, render_template, request, redirect
import logic
app = Flask(__name__)


# global variable used before adding the txt file to store data
# counter = {'GET':0, 'POST':0, 'DELETE':0, 'PUT':0}


@app.route('/')
def index():
    # global counter        comment: it was used before adding data.txt to store data
    counter = logic.file_read()
    return render_template('index.html', counter = counter)


@app.route('/request-counter', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def request_counter():
    # global counter        comment: it was used before adding data.txt to store data 
    counter = logic.file_read()
    counter[request.method] +=1
    logic.file_write(counter)
    return redirect('/')
    

@app.route('/statics')
def statics():
    counter = logic.file_read()
    return render_template('statics.html', counter = counter)



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 