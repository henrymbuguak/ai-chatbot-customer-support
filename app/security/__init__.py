from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address  # Use built-in IP detection

def init_security(app):
    """Enterprise security configuration"""

    talisman_config = app.config.get('TALISMAN_CONFIG', {})

    
    # Initialize Talisman first
    Talisman(
        app,
        content_security_policy=app.config['TALISMAN_CONFIG'].get('content_security_policy'),
        force_https=app.config['TALISMAN_CONFIG'].get('force_https', False),
        strict_transport_security=app.config['TALISMAN_CONFIG'].get('strict_transport_security', True),
        frame_options='DENY'
    )

    
    # Initialize Limiter with proper configuration
    limiter = Limiter(
        app=app,
        key_func=get_remote_address,
        default_limits=app.config["RATE_LIMITS"],
        headers_enabled=True,
        storage_uri="memory://",
        strategy="moving-window"
    )
    
    # Apply rate limits to all routes by default
    limiter.init_app(app)