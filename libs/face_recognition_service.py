import face_recognition
import PIL.Image
import numpy as np
import sys

class Face_recognition_service:
    def __init__(self, known_image, image_to_check):
        self.known_image = known_image
        self.image_to_check = image_to_check

    def booleanComparation(self):
        known_image2 = face_recognition.load_image_file(self.known_image) # pic from DUT
        result = None
        distance = 0
        known_face_encodings = face_recognition.face_encodings(known_image2)
        unknown_image = face_recognition.load_image_file(self.image_to_check)
        # Scale down image if it's giant so things run a little faster
        if max(unknown_image.shape) > 1600:
            pil_img = PIL.Image.fromarray(unknown_image)
            pil_img.thumbnail((1600, 1600), PIL.Image.LANCZOS)
            unknown_image = np.array(pil_img)

        unknown_encodings = face_recognition.face_encodings(unknown_image)

        for unknown_encoding in unknown_encodings:
            distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)
            result = list(distances <= 0.6)
        if result:
            return result[0]
    
    def scalarDiference(self):
        known_image2 = face_recognition.load_image_file(self.known_image) # pic from DUT
        result = None
        distances = 0
        known_face_encodings = face_recognition.face_encodings(known_image2)
        unknown_image = face_recognition.load_image_file(self.image_to_check)
        # Scale down image if it's giant so things run a little faster
        if max(unknown_image.shape) > 1600:
            pil_img = PIL.Image.fromarray(unknown_image)
            pil_img.thumbnail((1600, 1600), PIL.Image.LANCZOS)
            unknown_image = np.array(pil_img)

        unknown_encodings = face_recognition.face_encodings(unknown_image)

        for unknown_encoding in unknown_encodings:
            distances = face_recognition.face_distance(known_face_encodings, unknown_encoding)
            result = list(distances <= 0.6)

        return "%.2f" % distances[0]

if __name__ == "__main__":

    if sys.argv[1] == "booleanComparation":
        recognition_service = Face_recognition_service(sys.argv[2], sys.argv[3])
        result3 = recognition_service.booleanComparation()
        print(result3)

    if sys.argv[1] == "scalarDiference":
        recognition_service = Face_recognition_service(sys.argv[2], sys.argv[3])
        result3 = recognition_service.scalarDiference()
        print(result3)
