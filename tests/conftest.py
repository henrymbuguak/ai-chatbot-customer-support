import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config.from_object('instance.config.TestingConfig')
    app.config.update({
        'TESTING': True,
        'RATE_LIMITS': ["5 per minute"]
    })
    return app.test_client()