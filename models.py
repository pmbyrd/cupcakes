"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

DEFAULT_URL = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    
# todo cupcake model
# *include id, flavor, size, rating, image
class Cupcake(db.Model):
    # Todo make doc string
    """Model for cupcake table in database

    Args:
        db (Model): flavor(text), size(text), rating(float), image(text)
        
    Returns: An instance of a cupcake with flavor, size, rating, image and id
    """
    
    __tablename__ = "cupcakes"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=False, default=DEFAULT_URL)
    rating = db.Column(db.Float, nullable=False)

# *include serialize method for jsonifying

    def serialize(self):
        """Serialize a cupcake SQLAlchemy obj to dictionary
        
        Returns: 
            dict: Cupcake instance key value pairs
        
        """
        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }
        
    def __repr__ (self):
        """Shows a representation of a cupcake instance

        Returns:
            string: Cupcake instance key value pairs
        """
        return f"<Cupcake id={self.id} flavor={self.flavor} size={self.size} rating={self.rating} image={self.image}>"    
