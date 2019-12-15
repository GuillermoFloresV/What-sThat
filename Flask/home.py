from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import pathlib
from PIL import Image


from imageai.Detection import ObjectDetection
import os


#lines 104-114 thanks to these links:
#https://stackoverflow.com/questions/44926465/upload-image-in-flask
#https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
#This is critical to the code working
"""your path goes here!!"""
upload_folder = '/home/ocho/envs/final_project_whatsthat/What-sThat/Flask/static/images'
#allowed extensions is how we check if the file is going to be allowed
allowed_extensions = set(['png', 'jpg', 'jpeg'])



image_info = [
  {
    "id" : "36523127054_763afc5ed0_z",
    "title" : "Canoeing in Amsterdam",
    "flickr_user" : "bdodane"
  },
  {
    "id" : "36909037971_884bd535b1_z",
    "title" : "East Side Gallery",
    "flickr_user" : "Pieter van der Velden"
  },
  {
    "id" : "35889114281_85553fed76_z",
    "title" : "Quiet at dawn, Cabo San Lucas",
    "flickr_user" : "Erin Johnson"
  },
  {
    "id" : "37246779151_f26641d17f_z",
    "title" : "Rijksmuseum library",
    "flickr_user" : "John Keogh"
  },
  {
    "id" : "36140096743_df8ef41874_z",
    "title" : "Someday",
    "flickr_user" : "Thomas Hawk"
  },
  {
    "id" : "37198655640_b64940bd52_z",
    "title" : "Spreetunnel",
    "flickr_user" : "Jens-Olaf Walter"
  },
  {
    "id" : "cityGirl",
    "title" : "Chroma Velocity",
    "flickr_user" : "City Girl"
  }
]
def main_code():
  #test image
  inputted_image =  '37198655640_b64940bd52_z.jpg'

  execution_path = upload_folder

  detector = ObjectDetection()
  detector.setModelTypeAsRetinaNet()
  detector.setModelPath(
    os.path.join(
      execution_path,
      "resnet50_coco_best_v2.0.1.h5"))
  detector.loadModel()
  detections = detector.detectObjectsFromImage(
    input_image=os.path.join(
      execution_path, inputted_image), output_image_path=os.path.join(
        execution_path, "new.jpg"))

  # Maybe do a dictionary at the same time in order to count them and
  # display to the user how many times it saw a certain item. (maybe make
  # the text file downloadable as well as a download link of the extracted
  # images)
  list_of_items_found = []
  percentage_probability_of_item = []

  for eachObject in detections:
    list_of_items_found.append(eachObject["name"])
    percentage_probability_of_item.append(eachObject["percentage_probability"])

  #makes everything into a dictionary in order for better user readability (give code better formatting with object and the object percentage probability)
  my_dict = dict(zip(list_of_items_found, percentage_probability_of_item))


  #if the length of items found is greater than 0, then print out the dictionary to the user, else, let them know that the script found nothing and the program ends.
  if len(list_of_items_found) > 0:
    print(my_dict)
  else:
    print("Sorry, we could not find any items in this picture. Please try another image.")

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/successfullySubmitted', methods=['POST'])
def upload_picture():
  if request.method == "POST":
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
      file.save(os.path.join(app.config['upload_folder'], filename))
  return render_template('success.html', request.form['submittedImage',], inputted_image = inputted_image)


@app.route('/')
def home():
  return render_template('home.html',image=image_info)
if __name__=="__main__":
  app.run(debug=True)
