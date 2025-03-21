# **AI-Powered Chatbot for Customer Support**

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.2-green)
![Deepseek](https://img.shields.io/badge/Deepseek-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

Welcome to the **AI-Powered Chatbot for Customer Support** repository! This project demonstrates how to build a scalable, AI-driven chatbot using **Deepseek's Large Language Model (LLM)** and **Python Flask**. The chatbot is designed to handle customer inquiries, provide real-time responses, and integrate with external APIs for dynamic data retrieval.

This project is perfect for developers, AI enthusiasts, and businesses looking to automate customer support and reduce operational costs.

---

## **Features**
- **Natural Language Understanding**: Leverages Deepseek's LLM to process and respond to customer inquiries in natural language.
- **Real-Time Data Integration**: Connects to external APIs (e.g., inventory databases, weather services) to fetch dynamic information.
- **Contextual Conversations**: Maintains session context for personalized and intuitive interactions.
- **24/7 Availability**: Provides instant support without the need for human intervention.
- **Scalable Architecture**: Built with Flask for lightweight and flexible backend development.

---

## **Use Case: GreenGrocer Foods**
This project is inspired by **GreenGrocer Foods**, a leading online grocery delivery service. Their chatbot:
- Handles **80% of routine inquiries** automatically.
- Saves **$1.3 million annually** in operational costs.
- Provides **24/7 support** without additional hires.
- Improves customer satisfaction with faster response times.

---

## **Getting Started**

### **Prerequisites**
Before you begin, ensure you have the following:
- **Python 3.9 or higher**: [Download Python](https://www.python.org/downloads/)
- **Deepseek Account**: [Sign up for Deepseek](https://www.deepseek.com/) and top up $2 to use the API.
- **Basic knowledge of Python and Flask**.

---

### **Installation**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/henrymbuguak/ai-chatbot-customer-support.git
   cd ai-chatbot-customer-support
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Deepseek API Key**:
   - Rename the `.env_copy` file to `.env`.
   - Add your Deepseek API key to the `.env` file:
     ```bash
     DEEPSEEK_API_KEY=your_api_key_here
     ```

5. **Run the Flask app**:
   ```bash
   python manage.py
   ```
   Visit `http://127.0.0.1:5000/` in your browser to see the chatbot in action.

---

## **Project Structure**
```
ai-chatbot-customer-support/
│
├── app/                         # Main application code
│   ├── __init__.py              # Flask app initialization & Blueprint registration
│   ├── routes.py                # API route definitions
│   ├── models/                  # Database models (SQLAlchemy, if needed)
│   │   ├── __init__.py          # Initialize models package
│   │   ├── user.py              # User model
│   │   ├── chatbot.py           # Chatbot-related models
│   ├── utils/                   # Utility functions
│   │   ├── helpers.py           # Helper functions
│   │   ├── logger.py            # Logging configuration
│   │   └── validators.py        # Input validation functions
│   ├── services/                # Business logic layer
│   │   ├── chatbot_service.py   # AI chatbot logic
│   │   ├── user_service.py      # User-related business logic
│   ├── api/                     # API endpoints (Blueprints)
│   │   ├── __init__.py          # Register all APIs
│   │   ├── chatbot.py           # Chatbot API
│   │   ├── user.py              # User management API
│   │   ├── auth.py              # Authentication API
│   ├── templates/               # Jinja2 HTML templates (if needed)
│   ├── static/                  # Static assets (CSS, JS, images)
│
├── tests/                       # Unit and integration tests
│   ├── conftest.py              # Pytest fixtures
│   ├── test_routes/             # Tests for API routes
│   │   ├── test_chatbot.py
│   │   ├── test_user.py
│   ├── test_services/           # Business logic tests
│   ├── test_models/             # Database model tests
│   ├── test_utils/              # Utility function tests
│
├── docs/                        # Documentation
│   ├── architecture.md          # Architecture overview
│   ├── setup_guide.md           # Step-by-step setup instructions
│
├── instance/                    # Configuration files (ignored in Git)
│   ├── config.py                # Local config (for development)
│   ├── config.example.py        # Example config file
│
├── migrations/                  # Database migrations (Flask-Migrate)
│
├── logs/                        # Log files (optional)
│
├── .github/                     # GitHub-specific files
│   ├── ISSUE_TEMPLATE/          # Issue templates
│   ├── workflows/               # CI/CD workflows
│
├── .env_copy                    # Template for environment variables (rename to .env)
├── .gitignore                   # Specifies files to ignore in version control
├── Dockerfile                   # Docker configuration
├── docker-compose.yml           # Docker Compose configuration
├── Makefile                     # Common project commands (optional)
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Development dependencies
├── manage.py                    # Command-line utility for running the app
├── README.md                    # Project documentation
├── CONTRIBUTING.md              # Guidelines for contributors
├── LICENSE                      # Project license
```

---

## **Environment Variables**
To securely manage your API keys and other sensitive information:
1. Rename the `.env_copy` file to `.env`.
2. Add your Deepseek API key to the `.env` file:
   ```bash
   DEEPSEEK_API_KEY=your_api_key_here
   ```
3. Ensure `.env` is listed in your `.gitignore` file to prevent it from being tracked by Git.

---

## **How It Works**
1. A customer sends a query (e.g., "Where is my order?") through the frontend interface.
2. The query is sent to the Flask backend via an API endpoint.
3. The Flask backend processes the query and sends it to Deepseek's LLM.
4. Deepseek generates a response (e.g., "Your order is out for delivery and will arrive by 3 PM.").
5. The response is sent back to the frontend and displayed to the customer.

---

## **Contributing**
We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**
- **Deepseek**: For providing the powerful LLM that powers the chatbot.
- **Flask**: For the lightweight and flexible web framework.
- **GreenGrocer Foods**: For inspiring this real-world use case.

---

## **Contact**
Have questions or feedback? Feel free to reach out:
- **[Henry Mbugua](https://www.linkedin.com/in/henrymbugua/)**
- **GitHub Issues**: [Open an Issue](https://github.com/henrymbuguak/ai-chatbot-customer-support/issues)

---

## **Show Your Support**
If you find this project helpful, please give it a ⭐️ on GitHub!
