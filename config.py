class Config:
    SECRET_KEY = 'your_secret_key_here'  # Replace with a strong secret key
    DEBUG = True  # Set to False for production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'  # Use SQLite for simplicity; replace with your preferred database URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add other configuration options as needed
