import io
import string
from flask import Flask, request, jsonify
#from subprocess import call
from face1 import face
import socket
import json
import numpy as np
import base64
from PIL import Image
import cv2


#url = "http://140.114.233.91:8080"
host1 = '140.114.233.91'
port1 = 9999
app = Flask(__name__)

@app.route('/', methods = ['POST'])
def upload_file():
    try:
        file = request.files['file']
        print(file)
        file.save('C://Users//mnetlab//Downloads//ccproj//12.jpg')
        get = face()
        mysocket(get)
        return jsonify(status='ok')
            
#        requests.post(url, json=trsJson)
#                return '''
#    <!doctype html>
#    <title>Upload new File</title>
#    <h1>Upload new File</h1>
#    <form action="" method=post enctype=multipart/form-data>
#      <p><input type=file name=file>
#         <input type=submit value=Upload>
#    </form>
#    '''
    except Exception as e:
        print(e)
        return e

def mysocket(person):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host1, port1))
    cmd = person.encode()
    s.send(cmd)
    s.close()

if __name__ == '__main__':
    app.run(host = '140.114.79.165', port = 5000, debug = True)
    