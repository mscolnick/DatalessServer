from app import create_app, setup_database
import os
from config.development import SQLALCHEMY_DATABASE_URI


app = create_app('config.development')

if __name__ == '__main__':
    if not os.path.isfile(SQLALCHEMY_DATABASE_URI):
      setup_database(app)
    app.debug = True
    app.run()

