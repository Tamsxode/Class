from multiprocessing.dummy import Array


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score ):

        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, __name: str):
        self.name = __name
    

    def change_age(self, __age: int):
        self.age = __age

    def add_track(self, track):
        self.tracks.append(track)

    def get_score(self):
        return self.score
        
        

        pass



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

print(Bob.name)
print(Bob.age) 
print(Bob.tracks )
print(Bob.get_score())
