from typing import List
from numpy import ndarray
import face_recognition
from colorama import Fore, Style


class Person:
    id : str
    face_key_paths : List[str]
    face_reference_encodings : list[ndarray]

    def __init__(self , id: str , face_key_paths : List[str]) -> None:
        self.id = id
        self.face_key_paths = face_key_paths
        self.face_reference_encodings = self.get_face_reference_encodings_by_key_paths()
        
        
    def get_face_reference_encodings_by_key_paths(self):
        return_arr = []
        for key in self.face_key_paths:
            print(Fore.BLUE + "INFO:" + Style.RESET_ALL+ f"     Processing key {key}")
            return_arr.append(face_recognition.face_encodings(face_recognition.load_image_file(key))[0])
        return return_arr
