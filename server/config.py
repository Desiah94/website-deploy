# # Standard library imports

# # Remote library imports
# from flask import Flask
# from flask_cors import CORS
# from flask_migrate import Migrate
# from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData
# import os
# from dotenv import load_dotenv
# # Local imports

# # Instantiate app, set attributes
# load_dotenv()

# app = Flask(__name__,
#             static_url_path='', 
#             static_folder='../client/build', 
#             template_folder='../client/build')

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
# print("Database URI:", os.getenv('DATABASE_URI'))
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.json.compact = False

# # Define metadata, instantiate db
# metadata = MetaData(naming_convention={
#     "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
# })
# db = SQLAlchemy(metadata=metadata)
# migrate = Migrate(app, db)
# db.init_app(app)

# # Instantiate REST API
# api = Api(app)

# # Instantiate CORS
# CORS(app)
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__,
            static_url_path='', 
            static_folder='../client/build', 
            template_folder='../client/build')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
print("Database URI:", os.getenv('DATABASE_URI'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret')  # Fallback to 'super-secret' if not set

db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)
CORS(app)


# Ensure the Flask server hands over handling to React Router for undefined routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.template_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)  # Use host='0.0.0.0' to make server available on your network