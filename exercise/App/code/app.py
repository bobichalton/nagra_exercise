from flask import Flask, jsonify, request
import hashlib
import os
import datetime

app = Flask(__name__)

# Create the "uploads" folder if it doesn't exist
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# Store the uploaded images and their metadata in a dictionary
images = {}

# API endpoint for uploading images
@app.route('/image', methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = file.filename
    file_id = hashlib.sha256(filename.encode('utf-8')).hexdigest()
    file.save(os.path.join('uploads', file_id))
    metadata = {
        'id': file_id,
        'name': filename,
        'size': os.path.getsize(os.path.join('uploads', file_id)),
        'sha256': hashlib.sha256(open(os.path.join('uploads', file_id), 'rb').read()).hexdigest(),
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    images[file_id] = metadata
    return jsonify(metadata), 201

# API endpoint for retrieving image metadata
@app.route('/image/<file_id>', methods=['GET'])
def get_image_metadata(file_id):
    if file_id not in images:
        return 'Image not found', 404
    return jsonify(images[file_id]), 200

# API endpoint for retrieving duplicate images
@app.route('/image/duplicates', methods=['GET'])
def get_duplicate_images():
    duplicates = []
    hashes = {}
    for file_id, metadata in images.items():
        file_hash = metadata['sha256']
        if file_hash in hashes:
            duplicates.append(metadata)
            duplicates.append(hashes[file_hash])
        else:
            hashes[file_hash] = metadata
    return jsonify(duplicates), 200

# API endpoint for deleting images
@app.route('/image/<file_id>', methods=['DELETE'])
def delete_image(file_id):
    if file_id not in images:
        return 'Image not found', 404
    os.remove(os.path.join('uploads', file_id))
    metadata = images.pop(file_id)
    return jsonify(metadata), 200

# API endpoint for listing all images
@app.route('/list', methods=['GET'])
def list_images():
    return jsonify(list(images.values())), 200

# Metrics endpoint
@app.route('/metrics', methods=['GET'])
def metrics():
    # Define metrics and return as a JSON object
    metrics = {
        'total_images': len(images),
        'total_size': sum([metadata['size'] for metadata in images.values()])
        # Add more metrics as needed
    }
    return jsonify(metrics), 200

if __name__ == '__main__':
    app.run(debug=True)