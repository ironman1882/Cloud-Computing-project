from keras.models import model_from_json
from PIL import Image
import cv2 as cv
from keras.preprocessing import image
import numpy as np
from matplotlib import pyplot as plt 
from subprocess import call

def face():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    classifier = model_from_json(loaded_model_json)
    # load weights into new model
    classifier.load_weights("model.h5")
    print("Loaded model from disk")


    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    path='12.jpg'
    im = Image.open(path)
    img = cv.imread(path)
    faces = face_cascade.detectMultiScale(img, 1.2, 3)


    if faces != ():
        for x,y,w,h in faces:
            box = (x, y, x+w, y+h)
            crpim = im.crop(box).resize((64,64))
            target_image = image.img_to_array(crpim)
            target_image = np.expand_dims(target_image, axis = 0)
            res = classifier.predict_classes(target_image)[0]
            if res==0:
              people='Yu ming'
    
            else:
              people='other'
              call(["python", "C://Users//mnetlab//Downloads//SMTP_Email_2//SMTP_Email_2.py"])
              
    
            print("people:",people)
            cv.rectangle(img,(x,y),(x+w,y+h),(250,200,50),2)
            cv.putText(img,people, (x + int(w/3)-70, y-10), cv.FONT_HERSHEY_PLAIN, 2, (250,200,50), 2)
    
    
        #plt.figure(figsize=(30,20))
        plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    else:
        print("NO face")
        people='NO face'
        
    return people

