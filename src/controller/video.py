from libs import *


def get_chunk(byte1=None, byte2=None):
    full_path = 'static/NGYU.mp4'
    file_size = os.stat(full_path).st_size
    start = 0
    
    if byte1 < file_size:
        start = byte1
    if byte2:
        length = byte2 + 1 - byte1
    else:
        length = file_size - start

    with open(full_path, 'rb') as f:
        f.seek(start)
        chunk = f.read(length)
    return chunk, start, length, file_size

# KNOCKS OF MY FEET
def save():
    if 'video' in request.files:
        return redirect(request.url)
        ...
    file = request.files['video']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static', filename))
    return redirect(url_for('watch', v=filename))
        