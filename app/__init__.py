from flask import Flask
from dotenv import load_dotenv
from instance.config import (  # Add this import
    Config, 
    DevelopmentConfig, 
    ProductionConfig, 
    TestingConfig
)
from .utils.logger import configure_logging
from .security import init_security
from .routes import init_routes
import os

def create_app():
    # Load environment variables first
    env = os.getenv("FLASK_ENV", "production").lower()
    load_dotenv(f'.env.{env}')
    
    # Create app instance
    app = Flask(__name__)
    
    # Load configuration based on environment
    if env == 'development':
        app.config.from_object(DevelopmentConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(ProductionConfig)
    
    # Initialize components
    configure_logging()
    init_security(app)
    init_routes(app)
    
    return app