from models import storage
from models.base_model import BaseModel, Base, Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if storage.get_type() == 'db':
        reviews = relationship("Review", backref="place", cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals to the current Place.id"""
            from models.review import Review
            all_reviews = storage.all(Review)
            place_reviews = [review for review in all_reviews.values() if review.place_id == self.id]
            return place_reviews

    if storage.get_type() != 'db':
        @property
        def amenities(self):
            """Returns the list of Amenity instances based on the attribute amenity_ids"""
            from models.amenity import Amenity
            return [amenity for amenity in storage.all(Amenity).values() if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Adds an Amenity.id to the attribute amenity_ids"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
               