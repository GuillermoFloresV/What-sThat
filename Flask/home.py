# David Gaeta and Zaim Fuentes
# Date: 10/28/19
# Course: CST 205
# Abstarct: Sets up all of the backend for the website
# that displays images, and when clicked give
# more information on said image
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import random
import pathlib
from PIL import Image

image_info = [
  {
    "id" : "36523127054_763afc5ed0_z",
    "title" : "Canoeing in Amsterdam",
    "flickr_user" : "bdodane"
  },
  {
    "id" : "34694102243_3370955cf9_z",
    "title" : "Eastern",
    "flickr_user" : "Sean Davis"
  },
  {
    "id" : "36909037971_884bd535b1_z",
    "title" : "East Side Gallery",
    "flickr_user" : "Pieter van der Velden"
  },
  {
    "id" : "36604481574_c9f5817172_z",
    "title" : "Lombardia, september 2017",
    "flickr_user" : "Mónica Pinheiro"
  },
  {
    "id" : "36885467710_124f3d1e5d_z",
    "title" : "Palazzo Madama",
    "flickr_user" : "Kevin Kimtis"
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
    "id" : "34944112220_de5c2684e7_z",
    "title" : "View from our rental",
    "flickr_user" : "Doug Finney"
  }
]

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
  nums = random.sample(range(10),3)
  return render_template('home.html',image=image_info, rand=nums)
if __name__=="__main__":
  app.run(debug=True)