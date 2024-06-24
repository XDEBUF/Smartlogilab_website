


from flask import flash, request
from werkzeug.utils import secure_filename
from Config import Config
import os
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS
def save_on_server(file_up):
    if file_up not in request.files:
        flash('No file part')
        #return redirect(url_for('index'))
    file = file_up
    # if user.py does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
       # return redirect(url_for('index'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # TODO app.config[upload_folder]
        file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
        return filename