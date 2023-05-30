##Sets up the flask server for viewing the folder locally at {ip_address}:3001
from flask import Flask, render_template, send_from_directory, request, redirect
import os, subprocess
import getpass
import variables

app = Flask(__name__)
folderpath = variables.HS_path

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/folder')
@app.route('/folder/<path:foldername>')
def folder_index(foldername=None):
    folder_path = folderpath
    if foldername:
        folder_path = os.path.join(folder_path, foldername)
    command = f"ls -l {folder_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    files = result.stdout.splitlines()
    file_links = []

    for file in files:
        file_info = file.split()
        filename = file_info[-1]
        is_directory = file_info[0].startswith("d")

        if is_directory:
            if foldername:
                file_links.append({'filename': filename, 'path': f'/folder/{foldername}/{filename}/', 'is_folder': True})
            else:
                file_links.append({'filename': filename, 'path': f'/folder/{filename}/', 'is_folder': True})
        else:
            file_links.append({'filename': filename, 'path': f'/{filename}', 'is_folder': False})

    return render_template('folder_index.html', files=file_links)

@app.route('/<path:filename>')
def serve_file(filename):
    return send_from_directory(folderpath, filename, as_attachment=False)

@app.route('/folder/<path:foldername>/<path:filename>')
def serve_file2(foldername, filename):
    folder_path = folderpath
    if foldername:
        folder_path = os.path.join(folder_path, foldername)
    return send_from_directory(folder_path, filename, as_attachment=False)

@app.route('/launch-program')
def launch_program():
    folder_path=folderpath
    command =['sudo', '-S' 'python3', f'{folder_path}/tmp_file_properties.py']

    password = getpass.getpass("Enter your password: ")
    password = password + '\n'

    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
        output, error = process.communicate(input=password)

        if  process.returncode == 0:
            return "Program launched successfully!"
        else:
            return "Unable to run due to non super user status!"

    except subprocess.CalledProcessError as e:
        return "Error occurred while running the Sync! Login directly to continue."

"""
@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form['password']

        # Check if the password is correct
        if password == 'health':
            # Password is correct, redirect to the protected page
            return redirect('index.html')
        else:
            # Password is incorrect, show an error message
            error_message = 'Invalid password. Please try again.'
            return render_template('login.html', error_message=error_message)

    # Render the login page template
    return render_template('login.html')
"""
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename =file.filename
            file.save(folderpath + filename)
            return 'File uploaded successfully!'
    return render_template('upload.html')

if __name__== '__main__':
    app.run('0.0.0.0', port=3001)
    print("server is running at http://localhost:3001")