from flask import Flask, render_template, request, url_for, session, os, g
app = Flask(__name__)

# route
@app.route('/')
def index():
    return render_template('index.html', variableOne = variableOne, variableTwo = variableTwo )
    or:
    return 'Hello World"'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
    or: app.run(debug=True, use_reloader=True)
    and maybe: flask run --host=0.0.0.0 # to powinno odpalac nie tylko lokalnie ale z innych kompow rowniez 


# RECEIVING VARIABLE BY SERVER OPTION 1
@app.route('/user', default={'username' : 'dupa dupa'})
@app.route('/user/<username>')

def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

# RECEIVING VARIABLE BY SERVER  OPTION 2
@app.route('/post/<int:post_id>', methods = ['GET', 'POST']) #int: float: path: any: string:   GET, HEAD, POST, PUT, DELETE, OPTIONS
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

# # RECEIVING VARIABLE BY SERVER in URL OPTION 3
example url:  http://example.com/path/to/page?name=ferret&color=purple
name = ferret   ---> {'name':'ferret'}
color = purple  ---> {'color':'purple'}
accessing the variable: request.args['name'] or request.args[color]
example: 
        @app.route("/")
        def homepage():
            val = request.args.get('hello')
            return """Whats up, {x}""".format(x=val)

# CREATING THE URL in SERVER (url_for() method):
from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print url_for('index')                          gives result: /
    print url_for('login')                          gives result: /login
    print url_for('login', next='/')                gives result: /login?next=/
    print url_for('profile', username='John Doe')   gives result: /user/John%20Doe


# inside HTML variable and form actions
<form action="/whatev" method="get">  #meaning : When the user hits the Submit button, direct the browser to this URL".
      <input type="text" name="stuff" value="">
      <input type="submit" value="Submit">
  </form>

<input type="text" name="hello" value="">
<input type="submit" value="Submit">

# HIDDEN url data:
<input id="prodId" name="prodId" type="hidden" value="xm234jq">
ex. result will look like: title=My+excellent+blog+post&content=This+is+the+content+of+my+excellent+blog+post.+I+hope+you+enjoy+it!&postId=34657

# a to w server.py
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def homepage():
    return """
      <form action="/whatev" method="get">
        <input type="text" name="stuff" value="">
        <input type="submit" value="Submit">
      </form>"""

@app.route("/whatev")
def hooray():
     val = request.args.get('hello')
     return """Whats up, {x}""".format(x=val)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


# URL to CSS file 
url_for('static', filename='style.css')
The file has to be stored on the filesystem as static/style.css.
# in HTML HEAD
<link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">

# URL to javascript file 
<script src="demo_async.js" async></script>


# BACK BUTTON IN HTML
<a href="/">Back to home</a>
    # and in server.py:
    @app.route('/')
    def index():

# another example in html
<span>SUMMARY: show applicants table</span>
<a href="{{ url_for('show_applicant_table') }}">GET IT</a>
    # and in server.py:
    @app.route('/show_applicant_table')
def show_applicant_table():
    # We get back dictionaries here (for details check 'database_common.py')
    show_applicant_table = data_manager.get_show_applicant_table()
    return render_template('show_applicants_table.html', show_applicant_table=show_applicant_table)

# another one:
    <form action='/story/id/{{row}}' method="GET">
        <button type="submit"; value="edit"><i class="fas fa-pencil-alt"></i></button>
    </form>

# and in main.py
@app.route('/story/id/<row>', methods=['GET','POST'])
def story_by_id(row): #directs user to edit story (if method GET) or deletes story (if POST)
    if  request.method=="POST":
        data=persistance.get_data_from_file()



#files structure
# FLASK DEFAULT
/templates
    /page.html
/static
    /css 
    /img 
    /js 
main.py
logic.py



Case 1: a module:
/application.py
/templates
    /hello.html


Case 2: a package:
/application
    /__init__.py
    /templates
        /hello.html



# zmienne w html
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}



# HOW TO USE AN IMAGE AS A LINK
<a href="{{ url_for('delete_post', post_id=post.id) }}">
    <img href="{{ url_for('static', filename='images/logo.png') }}">
</a>

#ITERATION, FOR LOOP: variable navigation passed to html using render template
# navigation = [{
#         'href': '/',
#         'caption': 'Home'
#     },{
#         'href': '/contact',
#         'caption': 'Contact us'
#     }]
<body>
    <ul id="navigation">
        {% for item in navigation %}
            <li>
                <a href="{{ item.href }}">{{ item.caption }}</a>
            </li>
        {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}
    {# a comment #}
</body>


# ITERATING VIA DICT:
<dl>
{% for key, value in my_dict.iteritems() %}
    <dt>{{ key|e }}</dt>
    <dd>{{ value|e }}</dd>
{% endfor %}
</dl>



#generating <select> tag from the list of values:
<select name="country" id="country_selector">
    {% for country in countries %}
        <option value="{{country}}" {{'selected' if selected_country==country else ''}}>{{country}}</option>
    {% endfor %}
 </select>
To make this work, you'll need a route like this:
def route_edit():
    countries = ['Hungary', 'Poland', 'Germany', 'Italy']
    current = magic.get_selected_country()  # One of the options

    return render_template('edit.html', countries=countries, selected_country=current)

# Flask SESSIONS
dodac to w tym route ktory ma ustalac sesje i generowac session value
app.secret_key = 'secret_key_change_this_please'
#in flask app.py
app.secret_key = os.urandom(24)
#in a route
session['note'] = request.form['note']
#in anothr route
@app.route('/')
def route_index():
    note_text = None
    if 'note' in session:
        note_text = session['note']
    return render_template('index.html', note=note_text)

#in html
<p>
    {% if note is not none %} 
        {{ note }}
    {% else %}
        There is no saved notes.
    {% endif %}
</p>
#in html
<textarea id="note-input" name="note" rows="8" cols="80">{{ note }}</textarea>

#dropsession przy np. logout
session.pop("note", None)
return logged-out


import psycopg2


def main():
    try:
        # setup connection string
        connect_str = "dbname='yourdatabasename' user='yoursername' host='localhost' password='yourpassword'"
        
        # use our connection values to establish a connection
        connection = psycopg2.connect(connect_str)
        
        # set autocommit option, to do every query when we call it
        connection.autocommit = True
        
        # create a psycopg2 (client side) cursor that can execute queries
        cursor = connection.cursor()
        
        # removing the test table if it already exists
        cursor.execute("DROP TABLE IF EXISTS test;")
        
        # Execute a command: this creates a new table
        cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no more SQL injections!)
        cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

        # Query the database and obtain data as Python objects
        cursor.execute("SELECT * FROM test;")
        rows = cursor.fetchall()
        print(rows)

        # Close communication with the database
        cursor.close()

    except psycopg2.DatabaseError as exception:
        print(exception)

    finally:
        if connection:
            connection.close()

if __name__ == '__main__':
    main()








IP address :    internet protocol address np. 91.198.174.192.
DNS:            Domain Name System
ISP:            Internet service provider
router:         networking device
HTTP:           Hypertext Transfer Protocol
XML             eXtensible Markup Language (for storing and transporting data)
XHR             XMLHttpRequest, a default JS object

port:           a port is an endpoint of communication
URL:            Uniform Resource Locator 
HTML:           Hypertext Markup Language
CSS:            Cascading Style Sheets
JavaScript:     
Cookies:        small file on local devise, sesyjne i stałe
UserAgent:      aplickacja kliencka, naglowek zawierajact user agen string

SQL             Structured Query Language
PostgreSQL      powerful, open source object-relational database system
Query           precise request for information retrieval with database and information systems
ERD             Entity-relationship model or Entity-relationship Diagram
ASCII           American Standard Code for Information Interchange – siedmiobitowy system kodowania znaków
UTF-8           system kodowania Unicode, wykorzystujący od 1 do 6 bajtów do zakodowania pojedynczego znaku, w pełni kompatybilny z ASCII