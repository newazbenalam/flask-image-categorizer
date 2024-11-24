from flask import Flask, render_template, request, redirect, url_for
import os
import shutil

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'static/input')
CARTOON_DIR = os.path.join(BASE_DIR, 'static/cartoon_images')
PERSON_DIR = os.path.join(BASE_DIR, 'static/real_person')
UNCATEGORY_DIR = os.path.join(BASE_DIR, 'static/uncategory')

# Ensure category folders exist
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(CARTOON_DIR, exist_ok=True)
os.makedirs(PERSON_DIR, exist_ok=True)
os.makedirs(UNCATEGORY_DIR, exist_ok=True)

# Get all images in input directory
def get_images():
    return [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]

@app.route('/')
def index():
    images = get_images()
    if images:
        current_image = images[0]
    else:
        current_image = None
    return render_template('index.html', image=current_image)

@app.route('/filter/<category>/<filename>')
def filter_image(category, filename):
    src_path = os.path.join(INPUT_DIR, filename)
    if category == "cartoon":
        dest_dir = CARTOON_DIR
    elif category == "person":
        dest_dir = PERSON_DIR
    elif category == "uncategory":
        dest_dir = UNCATEGORY_DIR
    else:
        return redirect(url_for('index'))

    dest_path = os.path.join(dest_dir, filename)
    shutil.move(src_path, dest_path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
