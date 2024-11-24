# Image Classification Web App

This is a Flask-based web application that allows users to classify images into categories (Cartoon, Real Person, or Uncategorized) with additional filtering options. The selections are saved into an Excel file, making it ideal for manual image classification tasks with structured data output.

## Features

- Preview images one by one from a local directory.
- Classify images into predefined categories.
- Select filtering options for attributes like humor, sarcasm, offensiveness, motivation, and overall sentiment.
- Save classification results into an Excel file.
- User-friendly, responsive interface using Bootstrap.

---

## Installation Instructions

### Prerequisites

- Python 3.x installed on your system.
- A working internet connection to install required dependencies.
- Basic knowledge of Python and Flask.

### Steps to Set Up

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/image-classification-web-app.git
   cd image-classification-web-app
   ```

2. Set up a virtual environment:

   ```bash
   py -m venv .venv
   ```

3. Activate the virtual environment:

   ```bash
   .\venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r .\requirements.txt
   ```

5. Run the application:

   ```bash
   python .\app.py
   ```

---

## Usage Instructions

1. After starting the app, open your browser and navigate to:

   ```bash
   http://127.0.0.1:5000
   ```

2. **Preview Images**:
   - The application will display images one by one from the configured input directory.

3. **Classify Images**:
   - Use the dropdown menus to select filtering options for attributes like:
     - **Humor**: Funny, Not Funny, Very Funny
     - **Sarcastic**: Little Sarcastic, Not Sarcastic, Very Sarcastic
     - **Offensive**: Hateful Offensive, Slight Offensive, Not Offensive
     - **Motivational**: Motivational, Not Motivational
     - **Overall**: Very Negative, Negative, Neutral, Positive, Very Positive

4. **Save and Categorize**:
   - Click one of the action buttons (`Cartoon Image`, `Real Person`, or `Uncategorized`) to save the image into the corresponding folder and record the filtering options into the Excel file.

5. **Completion**:
   - Once all images are classified, a message will indicate that the task is complete.

---

## Folder Structure

```bash
image-classification-web-app/
│
├── app.py                   # Main Flask application script
├── requirements.txt         # Required Python dependencies
├── static/
│   ├── input/               # Folder containing images to classify
│   ├── output/              # Folders for classified images
│       ├── cartoon/
│       ├── person/
│       ├── uncategory/
├── templates/
│   ├── index.html           # HTML template for the web app
├── README.md                # Documentation
```

---

## Dependencies

This project uses the following Python libraries:

- Flask
- openpyxl
- Bootstrap (integrated via CDN)

---

## Future Enhancements

- Add bulk image upload functionality.
- Enable user-defined categories and filtering options.
- Provide visualization of classification results.

---

Feel free to contribute, report issues, or suggest features via the repository's [issues section](https://github.com/your-username/image-classification-web-app/issues).

Happy classifying! 🎉
