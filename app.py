from models import Product, Location, ProductMovement
from connectDB import app
from views.locationViews import index
from views.productViews import getProducts
from views.productMovementViews import getMovements

if __name__ == '__main__':
    app.run()

