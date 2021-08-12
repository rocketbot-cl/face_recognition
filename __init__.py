import os
import sys
from glob import glob
from subprocess import Popen, PIPE
import platform

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

import PIL.Image
import numpy as np
# face_recognition import main as face_main
from convertPdfToPng import convertPdfToPng
from  imageExtensionChecker import imageExtensionChecker

platform_name = platform.system()
path_to_poppler = None

def import_lib(relative_path, name, class_name=None):
    """
    - relative_path: library path from the module's libs folder
    - name: library name
    - class_name: class name to be imported. As 'from name import class_name'
    """
   
    import importlib.util

    cur_path = base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'libs' + os.sep

    spec = importlib.util.spec_from_file_location(name, cur_path + relative_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    if class_name is not None:
        return getattr(foo, class_name)
    return foo

if (platform_name == "Windows"):
    cv2 = import_lib('cv2/cv2.cp36-win32.pyd', 'cv2')
    path_to_poppler = base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'bin' + os.sep + 'bin' + os.sep



current_platform = platform.system()

executables = {
    "Windows": "win/face_recognition_service.exe",
    "Darwin": "mac/face_recognition_service"
}

module = GetParams("module")

filesSupported = ("jpeg","png","jpg", "pdf", "JPEG", "PNG", "JPG", "PDF")

try:
    

    
    if (module == "boolean_recognition"):
        distances = 0
        known_image = GetParams("known_image")
        image_to_check = GetParams("unknown_image")
        # # percentage = GetParams("percentage")
        result2 = GetParams("result")

        separator = '/'
        imageName = known_image
        imageToSearchIn = None
        newPathImage = None
        converted = False
        if not imageName.endswith(filesSupported):
            SetVar(result2, "File's type is not supported")
        else:
            if not (imageExtensionChecker(imageName)):
                newPathImage = convertPdfToPng(imageName, path_to_poppler)
                # imageToSearchIn = cv2.imread(newPathImage)
                converted = True
            else:
                # imageToSearchIn = cv2.imread(imageName)
                newPathImage = imageName
            
            # print(newPathImage)

            if (current_platform != "Linux"):

                a = Popen([base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'bin' + os.sep + executables[current_platform], 'booleanComparation', newPathImage, image_to_check],   stdout=PIPE)
                result = a.communicate()[0].decode()

            else:
                from face_recognition_service import Face_recognition_service
                newFace_recognition_service = Face_recognition_service(newPathImage, image_to_check)
                result = newFace_recognition_service.booleanComparation()
            if converted == True:
                os.remove(newPathImage)
                converted = False
            SetVar(result2, result)
            

    if (module == "scalar_distance_recognition"):

        distances = 0
        known_image = GetParams("known_image")
        image_to_check = GetParams("unknown_image")
        # # percentage = GetParams("percentage")
        result2 = GetParams("result")

        separator = '/'
        imageName = known_image
        imageToSearchIn = None
        newPathImage = None
        converted = False
        if not imageName.endswith(filesSupported):
            SetVar(result2, "File's type is not supported")
        else:
            if not (imageExtensionChecker(imageName)):
                newPathImage = convertPdfToPng(imageName, path_to_poppler)
                # imageToSearchIn = cv2.imread(newPathImage)
                converted = True
            else:
                # imageToSearchIn = cv2.imread(imageName)
                newPathImage = imageName

        if (current_platform != "Linux"):

            a = Popen([base_path + 'modules' + os.sep + 'face_recognition' + os.sep + 'bin' + os.sep + executables[current_platform], 'scalarDiference', newPathImage, image_to_check], stdout=PIPE)
            result = a.communicate()[0].decode()

        else:

            newFace_recognition_service = Face_recognition_service(newPathImage, image_to_check)
            result = newFace_recognition_service.scalarDiference()
        
        if converted == True:
            os.remove(newPathImage)
            converted = False
        result = 1 - float(result)
        SetVar(result2, "%.2f" % result)

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e