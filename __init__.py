import os
import sys
from glob import glob
from subprocess import Popen, PIPE

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

# from face_recognition_service import Face_recognition_service


module = GetParams("module")

try:
    if (module == "boolean_recognition"):
        distances = 0
        known_image = GetParams("known_image")
        image_to_check = GetParams("unknown_image")
        result2 = GetParams("result")

        a = Popen([base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'bin' + os.sep + 'win/face_recognition_service.exe', 'booleanComparation', known_image, image_to_check], stdout=PIPE)

        result = a.communicate()[0].decode()

        SetVar(result2, result)

    if (module == "scalar_distance_recognition"):

        distances = 0
        known_image = GetParams("known_image")
        image_to_check = GetParams("unknown_image")
        result2 = GetParams("result")

        a = Popen([base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'bin' + os.sep + 'win/face_recognition_service.exe', 'scalarDiference', known_image, image_to_check], stdout=PIPE)

        result = a.communicate()[0].decode()

        SetVar(result2, 1 - float(result))

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
    PrintException()
    raise e