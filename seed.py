from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor="red velvet",
    size = "medium",
    rating = 7,
    image = "https://images.unsplash.com/photo-1614707267537-b85aaf00c4b7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Y3VwY2FrZXN8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"
)

c4 = Cupcake(
    flavor="vanilla",
    size = "medium",
    rating = 8,
    image = "https://images.unsplash.com/photo-1519869325930-281384150729?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTZ8fHZhbmlsbGElMjBjdXBjYWtlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
)

db.session.add_all([c1, c2, c3, c4])
db.session.commit()