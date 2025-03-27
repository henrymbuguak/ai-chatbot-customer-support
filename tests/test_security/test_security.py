import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()

def test_rate_limiting(client):
    """Verify API rate limiting prevents abuse"""
    # Test against configured 5 requests/minute
    for _ in range(5):
        response = client.post('/api/v1/chat', json={'query': 'valid question'})
        assert response.status_code == 200
    
    # 6th request should fail
    response = client.post('/api/v1/chat', json={'query': 'test'})
    assert response.status_code == 429, f"Expected 429, got {response.status_code}"
    assert "5/minute" in response.json['error']

def test_security_headers(client):
    """Validate security headers exist"""
    response = client.post('/api/v1/chat', json={'query': 'test'})
    headers = response.headers
    
    assert 'Strict-Transport-Security' in headers, "Missing HSTS header"
    assert headers['X-Content-Type-Options'] == 'nosniff', "X-Content-Type mismatch"
    assert headers['Content-Security-Policy'] == "default-src 'self'", "Invalid CSP"
    assert headers['X-Frame-Options'] == 'DENY', "Missing frame protection"


def test_error_logging(mocker, client):
    """Ensure errors are logged properly"""
    mock_logger = mocker.patch('app.services.chatbot_service.logger.error')
    
    # Trigger empty query
    response = client.post('/api/v1/chat', json={'query': ''})
    
    mock_logger.assert_called_once_with(
        "api_failure",
        error="Please provide a valid question",
        query="",
        client_ip='127.0.0.1',
        stack_trace=mocker.ANY,  # Flexible match
        error_code="EMPTY_QUERY_001",
        support_contact="support@greengrocer.com",
        response_id=mocker.ANY,  # Flexible match for UUID
        timestamp=mocker.ANY,    # Flexible match for timestamp
        assistant_version=mocker.ANY,
        processing_time=mocker.ANY
    )
    assert response.status_code == 400
