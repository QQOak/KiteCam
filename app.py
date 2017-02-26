#!/usr/bin/python3 

from flask import Flask, jsonify
from flask import render_template

from time import sleep
from fractions import Fraction

import picamera

import os
#from os import listdir
#from os.path import isfile, join

app = Flask(__name__)




def getHighestFileNumber():
	count = 0
	photosPath = os.path.join(app.root_path, 'static/photos/')
	
	for filename in os.listdir(photosPath):
		count = count + 1

	return count



filenumber = getHighestFileNumber()

@app.route("/api/takepicture")
def apiTakePicture():
	#TODO:
	# Just return the filename of the picture taken
	# Or return the thumbnail inline and the filename of the picture taken


	
	global filenumber
	filename = "image%04d.jpg" % filenumber
	
	
	with picamera.PiCamera() as camera:
		camera.hflip = True
		camera.vflip = True
		
	#	camera.resolution = (2592, 1944)
	#	camera.resolution = (800, 600)
	#	camera.resolution = (1980, 1920) # Full HD
		
		
		camera.resolution = (1280, 720) # HD Ready
		sleep(1)
		
		camera.capture('static/photos/%s' % filename)
		filenumber = filenumber + 1
		
	
	return jsonify( Filename = filename )
	
	
@app.route("/api/settings")
def apiSettings():
	#TODO:
	# Expect 
	return 0

@app.route("/countFiles")
def countFiles():
	return "the number of files is %d" % getHighestFileNumber()


@app.route("/recordvideo")
def recordVideo():
	return ""

@app.route("/takepicture")
def takePicture():
	#TODO:
	# Display an interface to 
	return render_template('template.html', Title='Take Picture' )
	

@app.route('/listphotos')
def listPhotos():

	result = ""
	photosPath = os.path.join(app.root_path, 'static/photos/')
	
	for filename in os.listdir(photosPath):
		result = result + "<div>%s</div>" % filename

	return result
	
@app.route("/")
def index():
	return render_template('template.html')

if __name__ == "__main__":
	
    app.run(debug=True, host="0.0.0.0")
