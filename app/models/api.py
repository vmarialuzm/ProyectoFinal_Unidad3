import datetime
class Api():
    def __init__(self,id,name,status,species,gender,first_location,last_location,n_episodes,image,created):
        self.id=id
        self.name=name
        self.status=status
        self.species=species
        self.gender=gender
        self.first_location=first_location
        self.last_location=last_location
        self.n_episodes=n_episodes
        self.image=image
        self.created=created

    def to_json(self):
        return{
            'id':self.id,
            'name':self.name,
            'status':self.status,
            'species':self.species,
            'gender':self.gender,
            'first_location':self.first_location,
            'last_location':self.last_location,
            'n_episodes':self.n_episodes,
            'image':self.image,
            'created': self.created
        }
    