from flask import Flask

app = Flask(__name__)

# ... Other configurations and extensions

# Register your blueprints or routes here
from app.main import main_bp
app.register_blueprint(main_bp)

# ...
