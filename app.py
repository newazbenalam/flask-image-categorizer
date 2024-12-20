from flask import Flask, render_template, request, redirect, url_for
import os
import shutil
from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.table import Table
from openpyxl.worksheet.filters import AutoFilter
from datetime import datetime

app = Flask(__name__)

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(BASE_DIR, 'static/input')
CARTOON_DIR = os.path.join(BASE_DIR, 'static/cartoon_images')
PERSON_DIR = os.path.join(BASE_DIR, 'static/real_person')
UNCATEGORY_DIR = os.path.join(BASE_DIR, 'static/uncategory')
LOG_FILE = os.path.join(BASE_DIR, 'Image_Categorization_Log.xlsx')

# Ensure category folders exist
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(CARTOON_DIR, exist_ok=True)
os.makedirs(PERSON_DIR, exist_ok=True)
os.makedirs(UNCATEGORY_DIR, exist_ok=True)

# Initialize Excel log file if not exists
def initialize_log():
    if not os.path.exists(LOG_FILE):
        wb = Workbook()
        ws = wb.active
        ws.title = "Log"
        ws.append(["Image ID", "Humour", "Sarcastic", "Offensive", "Motivational", "Overall", "Category", "Timestamp"])
        wb.save(LOG_FILE)
        wb.close()

# Get all images in input directory
def get_images():
    return [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]

# Log categorization action

# Log categorization action with AutoFilter
def log_action(image_id, humour, sarcastic, offensive, motivational, overall, category):
    # Check if the log file exists, if not, create it
    if not os.path.exists(LOG_FILE):
        # Create a new workbook and sheet
        wb = Workbook()
        ws = wb.active
        ws.title = "Log"
        
        # Create the header row
        headers = ["Image ID", "Humour", "Sarcastic", "Offensive", "Motivational", "Overall", "Category", "Timestamp"]
        ws.append(headers)

        # Apply AutoFilter to the header row
        ws.auto_filter.ref = "A1:H1"  # Set filter range for the headers

        # Save the workbook
        wb.save(LOG_FILE)
    else:
        # Load the existing workbook
        wb = load_workbook(LOG_FILE)
        ws = wb.active
        
        # Apply AutoFilter if not already applied (check for existing filter range)
        if not ws.auto_filter.ref:
            ws.auto_filter.ref = "A1:H1"  # Apply AutoFilter to the headers

    # Append the new log entry as a row
    row = [
        image_id,
        humour,
        sarcastic,
        offensive,
        motivational,
        overall,
        category,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ]
    
    ws.append(row)

    # Save the updated workbook
    wb.save(LOG_FILE)
    
    
    
@app.route('/', methods=['GET', 'POST'])
def index():
    images = get_images()
    if images:
        current_image = images[0]
    else:
        current_image = None

    if request.method == 'POST':
        # Collect classification inputs
        image_id = request.form.get("image_id")
        humour = request.form.get("humour")
        sarcastic = request.form.get("sarcastic")
        offensive = request.form.get("offensive")
        motivational = request.form.get("motivational")
        overall = request.form.get("overall")
        category = request.form.get("category")

        # Move the image to the selected category folder
        src_path = os.path.join(INPUT_DIR, image_id)
        if category == "cartoon":
            dest_dir = CARTOON_DIR
        elif category == "person":
            dest_dir = PERSON_DIR
        elif category == "uncategory":
            dest_dir = UNCATEGORY_DIR
        else:
            return redirect(url_for('index'))

        dest_path = os.path.join(dest_dir, image_id)
        shutil.move(src_path, dest_path)

        # Log the action to the Excel file
        log_action(image_id.split('.')[0], humour, sarcastic, offensive, motivational, overall, category)

        return redirect(url_for('index'))

    # remaining_images = get_remaining_images()  # Function to fetch remaining images
    return render_template('index.html', image=current_image)

# Get remaining images from the input directory
def get_remaining_images():
    """
    Fetches the list of remaining images in the input folder.

    Returns:
        list: Sorted list of filenames of remaining images in the input directory.
    """
    # List only image files in the input folder
    images = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('png', 'jpg', 'jpeg', 'gif'))]
    return sorted(images)

if __name__ == '__main__':
    initialize_log()  # Ensure log file is ready
    app.run(debug=True)
