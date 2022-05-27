class Student:
    
    
    def __init__(self, name, age, tracks, score):
        
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        

    def get_score(self):    
        return self.score 

    def change_name(self, name):
        self.name = name
        print (self.name)
    
    def change_age(self, age):
        self.age = age
        print (self.age)

    def add_track(self, tracks):
        self.tracks.append(tracks)
        print (self.tracks)        

bob = Student("Bob", age=26, tracks=["FE","BE"],score=20.90)
    
print('Student details:')  
print('The name of the student is', bob.name)
print('Age: ', bob.age)
print('Tracks: ', bob.tracks)
print('Score: ',bob.score)

# Expected methods
bob.change_name("Peter")
bob.change_age(34)
bob.add_track("UI/UX")
bob.get_score()

