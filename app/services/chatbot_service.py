import uuid
from datetime import datetime
from typing import Dict, Optional
import structlog
from deepseek import DeepSeekAPI  # Using the provided class
import os

logger = structlog.get_logger()

class ChatbotService:
    """Handles AI-powered customer support interactions"""
    
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            logger.critical("config_error", message="Missing API key")
            raise ValueError("Deepseek API key not configured")
        
        self.client = DeepSeekAPI(api_key=self.api_key)
        logger.info("service_initialized")

    def generate_response(self, user_query: str, user_ip: Optional[str] = None) -> Dict[str, any]:
        """Process customer queries with comprehensive tracking"""
        response_id = str(uuid.uuid4())
        start_time = datetime.utcnow()
        metadata = {
            "response_id": response_id,
            "timestamp": start_time.isoformat(),
            "client_ip": user_ip,
            "assistant_version": "GreenGrocer AI 1.4.2",
            "processing_time": 0.0,
            "error_code": None,
            "support_contact": "support@greengrocer.com"
        }

        try:
            if not user_query.strip():
                metadata["error_code"] = "EMPTY_QUERY_001"
                logger.error(
                    "api_failure",
                    error="Please provide a valid question",
                    query=user_query,
                    client_ip=user_ip,
                    stack_trace=self._safe_get_stacktrace(Exception("Empty query")),
                    error_code="EMPTY_QUERY_001",
                    support_contact="support@greengrocer.com",
                    response_id=str(uuid.uuid4()),
                    timestamp=datetime.utcnow().isoformat(),
                    assistant_version="GreenGrocer AI 1.4.2",
                    processing_time=0.0
                )

                return {
                    "content": "Please provide a valid question",
                    "metadata": metadata
                }

            # Handle known FAQs
            query = user_query.lower()
            if "delivery hours" in query:
                metadata["processing_time"] = self._calculate_processing_time(start_time)
                return {
                    "content": "Delivery available Mon-Sat 8:00 AM - 8:00 PM EST. "
                              "Same-day cutoff: 12:00 PM EST.",
                    "metadata": metadata
                }

            if "order status" in query:
                metadata["processing_time"] = self._calculate_processing_time(start_time)
                return {
                    "content": "Your order is en route with estimated arrival by 3:00 PM EST. "
                              "Track your order at https://track.greengrocer.com",
                    "metadata": metadata
                }

            # AI-generated response
            messages = [
                {
                    "role": "system",
                    "content": "You are a customer support agent for GreenGrocer Foods. "
                              "Respond professionally with EST timezone references. "
                              "Keep answers under 500 characters."
                },
                {
                    "role": "user",
                    "content": user_query
                }
            ]

            ai_response = self.client.chat_completion(
                prompt=messages,
                model="deepseek-chat",
                temperature=0.7,
                max_tokens=500,
                stream=False
            )

            metadata["processing_time"] = self._calculate_processing_time(start_time)
            logger.info(
                "api_success",
                query=user_query,
                response_length=len(ai_response),
                **metadata
            )

            return {
                "content": ai_response,
                "metadata": metadata
            }

        except Exception as e:
            metadata.update({
                "processing_time": self._calculate_processing_time(start_time),
                "error_code": self._get_error_code(e),
                "stack_trace": self._safe_get_stacktrace(e)
            })
            
            logger.error(
                "api_failure",
                error=str(e),
                query=user_query,
                **metadata
            )

            return {
                "content": self._get_user_friendly_error(e),
                "metadata": metadata
            }

    def _calculate_processing_time(self, start_time: datetime) -> float:
        return round((datetime.utcnow() - start_time).total_seconds(), 3)

    def _get_error_code(self, error: Exception) -> str:
        error_msg = str(error)
        if "HTTP Error 429" in error_msg:
            return "RATE_LIMIT_429"
        if "HTTP Error 5" in error_msg:
            return "SERVER_ERROR_500"
        return "CLIENT_ERROR_400"

    def _get_user_friendly_error(self, error: Exception) -> str:
        error_code = self._get_error_code(error)
        return {
            "RATE_LIMIT_429": "Our systems are busy. Please try again in a minute.",
            "SERVER_ERROR_500": "We're experiencing technical difficulties. Our team has been notified.",
            "CLIENT_ERROR_400": "Invalid request. Please check your input."
        }.get(error_code, "An unexpected error occurred. Please contact support.")

    def _safe_get_stacktrace(self, error: Exception) -> str:
        try:
            return str(error.__traceback__)
        except Exception:
            return "Stacktrace unavailable for security reasons"