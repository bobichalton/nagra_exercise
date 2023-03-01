# Flask Image Uploader

A simple Flask application for uploading and managing images.

## Requirements

Python 3.6 or higher
Flask
hashlib
datetime

#Installation
Clone the repository:

```bash
git clone https://github.com/your-username/flask-image-uploader.git
```

```bash
cd flask-image-uploader
```
##Install the dependencies:

```bash
pip install -r requirements.txt
```
## Usage

Run the Flask application:

```bash
python app.py
```
Use a tool such as Postman to interact with the API.

To upload an image, send a POST request to http://localhost:5000/image with the image file as the request body.

To retrieve image metadata, send a GET request to http://localhost:5000/image/<file_id>.

To retrieve duplicate images, send a GET request to http://localhost:5000/image/duplicates.

To delete an image, send a DELETE request to http://localhost:5000/image/<file_id>.

o list all uploaded images, send a GET request to http://localhost:5000/list.

To retrieve metrics about the uploaded images, send a GET request to http://localhost:5000/metrics.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## License

[MIT](https://choosealicense.com/licenses/mit/)

