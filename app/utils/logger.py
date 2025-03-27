import structlog
import logging
import os

def configure_logging():
    """Configures structured logging with proper file handling"""
    
    # Create logs directory if not exists
    os.makedirs('logs', exist_ok=True)
    
    # Configure structlog
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ],
        wrapper_class=structlog.BoundLogger,
        context_class=dict,
        logger_factory=structlog.WriteLoggerFactory(
            file=open('logs/app.log', 'a')  # Direct file handle instead of FileHandler
        )
    )