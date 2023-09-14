import person
import os, sys  ,face_recognition , shutil, time, Errors
from multiprocessing import Pool, Process
from typing import List
from colorama import Fore, Style
import cv2


#region scanner_functions
def scan_directory(directory):
    """
    directory : string -> Use relative or absolut path
    """
    r = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            r.append(os.path.join(root, file))
    return r             
    # return [list(map(lambda x : os.path.join(root  , x) , files)) for root , dirs , files in os.walk(directory)]


def get_people_by_keys_paths(keys:str) -> List[person.Person]:
    people = []
    rdf = list(os.walk(keys))
    for people_paths in range(len(rdf[0][1])):
        tmp = [os.path.join(rdf[people_paths+1][0] , img) for img in rdf[people_paths+1][2]]
        people.append(person.Person(
            id=rdf[0][1][people_paths],
            face_key_paths=tmp
        ))

    return people
#endregion

class ImageProcessor:
    def __init__(self , people:List[person.Person] , images:list[str] ) -> None:
        # self.person = person
        self.people = people
        self.images = images
        #Can't use batch face locations because of the diffeneces of dimension of photos
        

    def scan_for_people(self):
        pool = Pool(processes=8)

        print(Fore.BLUE + "INFO:" + Style.RESET_ALL+"     Starting multiprocessing ...")
        res = pool.imap_unordered(self.process_image , range(len(self.images)))
        for r in res:
            if r[0] == 1:
                print(Fore.GREEN + "RESULT:" + Style.RESET_ALL+  f"     Found {len(r[3])} match(es) in {r[1]}, took [{r[2]}s]")
            else:
                print(Fore.RED + f"RESULT:"  + Style.RESET_ALL+  f"     No match in {r[1]}, took [{r[2]}s]")

        

    def process_image(self , image):
        print(Fore.YELLOW+"Process:"+Style.RESET_ALL+f"    Process image {image+1} / {len(self.images)} ({self.images[image]})")
        start = time.time()
        numpy_image = face_recognition.load_image_file(self.images[image]) 
        face_loaction = face_recognition.face_locations(numpy_image, number_of_times_to_upsample=1)
        res = [1 , self.images[image] , None , []]
        for face in face_recognition.face_encodings(numpy_image , face_loaction):
            for person in self.people:
                if True in face_recognition.compare_faces(person.face_reference_encodings, face , tolerance=0.47):
                    shutil.copy(self.images[image] , f"./out/{person.id}/{os.path.basename(self.images[image])}")  
                    end = time.time()
                    res[2] = end-start
                    res[3].append(person.id)
        end = time.time()
        if len(res[3]) > 0:
            return res
        else: 
            return [0 , self.images[image] ,(end-start) , None]


if __name__ == "__main__":
    #Create .\out\ path in cwd
    if not os.path.isdir(f"./out/"):
        os.makedirs(f"./out/")

    #region Argument handling
    #Get images
    try:
        resource_path = sys.argv[1]
        if not os.path.exists(resource_path): raise Errors.PathDoesNotExistError(resource_path)
    except IndexError:
        print("Error: Missing argument");exit()

    #Get keys
    try:
        if sys.argv[2] == "--keys":
            arg3 = sys.argv[3]
            if not os.path.exists(arg3):
                raise Errors.PathDoesNotExistError(arg3)
            else: 
                keys = arg3
    except IndexError:
        print("Error: Missing argument");exit()
    #endregion        

    print(Fore.BLUE + "INFO:" + Style.RESET_ALL+"     Starting program ...")
    start_time = time.time()
    images = scan_directory(resource_path)
    people = get_people_by_keys_paths(keys)

                    
    for p in people:
        if not os.path.isdir(f"./out/{p.id}"):
            os.makedirs(f"./out/{p.id}")
    ImageProcessor(people , images).scan_for_people()
    end_time = time.time()
    o = [len(os.listdir(f'./out/{p.id}')) for p in people]
    print(Fore.BLUE+"INFO:"+ Style.RESET_ALL+ f"       Program finished in [{end_time - start_time}] , found {sum(o)} matches")