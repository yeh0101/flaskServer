from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='ESP32 Image Viewer')
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route to display image gallery
@app.route('/')
def gallery():
    images = os.listdir(UPLOAD_FOLDER)
    images = [img for img in images if img.lower().endswith(('.jpg', '.jpeg', '.png'))]
    return render_template('gallery.html', images=images)

# Route to serve image files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Run the app
if __name__ == '__main__':
    print('Starting Flask image viewer...')
    app.run(host='0.0.0.0', port=5000)
