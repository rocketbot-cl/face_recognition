import os
import sys
import subprocess
import cv2
from glob import glob
import time
import subprocess

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

import face_recognition
import PIL.Image
import numpy as np
# face_recognition import main as face_main


module = GetParams("module")

try:
    if (module == "boolean_recognition"):
        distances = 0
        known_image = GetParams("known_image")
        image_to_check = GetParams("unknown_image")
        # # percentage = GetParams("percentage")
        result2 = GetParams("result")

        known_image = face_recognition.load_image_file(known_image) # pic from DUT
        # print(known_image)
        known_face_encodings = face_recognition.face_encodings(known_image)


        unknown_image = face_recognition.load_image_file(image_to_check)

        # Scale down image if it's giant so things run a little faster
        if max(unknown_image.shape) > 1600:
            pil_img = PIL.Image.fromarray(unknown_image)
            pil_img.thumbnail((1600, 1600), PIL.Image.LANCZOS)
            unknown_image = np.array(pil_img)

        unknown_encodings = face_recognition.face_encodings(unknown_image)

        for unknown_encoding in unknown_encodings:
            distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)
            result = list(distances <= 0.6)

        if True in result:
            SetVar(result2, True)
        else:
            SetVar(result2, False)

    if (module == "scalar_distance_recognition"):

        distances = 0
        known_image = GetParams("known_image")
        image_to_check = GetParams("unknown_image")
        # # percentage = GetParams("percentage")
        result2 = GetParams("result")

        known_image = face_recognition.load_image_file(known_image) # pic from DUT
        # print(known_image)
        known_face_encodings = face_recognition.face_encodings(known_image)


        unknown_image = face_recognition.load_image_file(image_to_check)

        # Scale down image if it's giant so things run a little faster
        if max(unknown_image.shape) > 1600:
            pil_img = PIL.Image.fromarray(unknown_image)
            pil_img.thumbnail((1600, 1600), PIL.Image.LANCZOS)
            unknown_image = np.array(pil_img)

        unknown_encodings = face_recognition.face_encodings(unknown_image)

        for unknown_encoding in unknown_encodings:
            distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)
            result = list(distances <= 0.6)

        SetVar(result2, "%.2f" % distances[0])

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
    PrintException()
    raise e