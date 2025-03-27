from flask import jsonify, request, current_app
from .services.chatbot_service import ChatbotService
from flasgger import swag_from

def init_routes(app):
    chatbot = ChatbotService()
    
    @app.route(f'{app.config["API_VERSION"]}/chat', methods=['POST'])
    @swag_from({
        "tags": ["Customer Support"],
        "description": "AI-powered customer query resolution",
        "parameters": [{
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                }
            }
        }],
        "responses": {
            200: {
                "description": "AI-generated response",
                "schema": {
                    "type": "object",
                    "properties": {
                        "version": {"type": "string"},
                        "response": {"type": "string"},
                        "security": {
                            "type": "object",
                            "properties": {
                                "https_enforced": {"type": "boolean"},
                                "rate_limit": {"type": "string"},
                                "client_ip": {"type": "string"}
                            }
                        }
                    }
                }
            }
        }
    })

    def handle_chat():
        """Chat endpoint with proper rate limit tracking"""
        user_query = request.json.get('query', '').strip()
        user_ip = request.remote_addr
        
        if not user_query:
            return jsonify({
                "error": "Empty query received",
                "code": "INVALID_QUERY_400"
            }), 400
            
        # Get chatbot response
        chatbot_response = chatbot.generate_response(user_query, user_ip)
        
        # Get rate limit info from headers
        rate_limit_info = {
            "limit": request.headers.get("X-RateLimit-Limit"),
            "remaining": request.headers.get("X-RateLimit-Remaining"),
            "reset": request.headers.get("X-RateLimit-Reset")
        }
        
        return jsonify({
            "version": current_app.config["API_VERSION"],
            "content": chatbot_response["content"],
            "metadata": chatbot_response["metadata"],
            "security": {
                "client_ip": user_ip,
                "https_enforced": current_app.config["TALISMAN_CONFIG"]["force_https"],
                "rate_limit": rate_limit_info
            },
            "actions": [
                {
                    "type": "schedule_delivery",
                    "title": "View Delivery Slots",
                    "url": f"{current_app.config['API_VERSION']}/delivery-slots"
                }
            ]
        })