import os
import sys
from glob import glob
from subprocess import Popen, PIPE
import platform

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

import face_recognition
import PIL.Image
import numpy as np
# face_recognition import main as face_main

from face_recognition_service import Face_recognition_service

current_platform = platform.system()

executables = {
    "Windows": "win/face_recognition_service.exe",
    "Darwin": "mac/face_recognition_service"
}

module = GetParams("module")

try:
    if (module == "boolean_recognition"):
        distances = 0
        known_image = GetParams("known_image")
        image_to_check = GetParams("unknown_image")
        # # percentage = GetParams("percentage")
        result2 = GetParams("result")

        if (current_platform != "Linux"):

            a = Popen([base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'bin' + os.sep + executables[current_platform], 'booleanComparation', known_image, image_to_check], stdout=PIPE)
            result = a.communicate()[0].decode()
            
        else:

            newFace_recognition_service = Face_recognition_service(known_image, image_to_check)
            result = newFace_recognition_service.booleanComparation()

        SetVar(result2, result)

    if (module == "scalar_distance_recognition"):

        distances = 0
        known_image = GetParams("known_image")
        image_to_check = GetParams("unknown_image")
        # # percentage = GetParams("percentage")
        result2 = GetParams("result")

        if (current_platform != "Linux"):

            a = Popen([base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'bin' + os.sep + executables[current_platform], 'scalarDiference', known_image, image_to_check], stdout=PIPE)
            result = a.communicate()[0].decode()

        else:

            newFace_recognition_service = Face_recognition_service(known_image, image_to_check)
            result = newFace_recognition_service.scalarDiference()

        SetVar(result2, 1 - float(result))

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
    PrintException()
    raise e