from bottle import route, run, template,request

import os

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/login',method="get")
def loginPage():
    return """
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        <form action="/login" method="post">
            <input value="AlterPassword" type="submit">
        </form>
    """
@route('/login',method="post")
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username=="admin" and password=="abc123,":
        return """
                <form action="/upload" method="post" enctype="multipart/form-data">
                Category:      <input type="text" name="category" />
                Select a file: <input type="file" name="upload" />
                <input type="submit" value="Start upload" />
                </form>
            """
    else:
        return "Login failed!"

@route('/upload',method="get")
def uploadPage():

    return """
        <form action="/upload" method="post" enctype="multipart/form-data">
        Category:      <input type="text" name="category" />
        Select a file: <input type="file" name="upload" />
        <input type="submit" value="Start upload" />
        </form>
    """

@route('/upload',method="post")
def uploadFile():
    category = request.forms.get('category')
    upload = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.lua'):
        return 'File extension not allowed.'

    #save_path = get_save_path_for_category(category)
    save_path="/usr/local/freeswitch/scripts/"+category
    upload.save(save_path,overwrite=True)  # appends upload.filename automatically
    return 'OK'
run(host='localhost', port=8080)