# **Contributing to AI-Powered Chatbot for Customer Support**

Thank you for your interest in contributing to the **AI-Powered Chatbot for Customer Support** project! We welcome contributions from developers, AI enthusiasts, and anyone passionate about building innovative solutions for customer support.

This guide will walk you through the process of contributing to the project. Whether you’re fixing a bug, adding a feature, or improving documentation, your contributions are highly appreciated.

---

## **Table of Contents**
1. [Code of Conduct](#code-of-conduct)
2. [How to Contribute](#how-to-contribute)
   - [Reporting Bugs](#reporting-bugs)
   - [Suggesting Enhancements](#suggesting-enhancements)
   - [Submitting Code Changes](#submitting-code-changes)
3. [Setting Up the Project](#setting-up-the-project)
4. [Pull Request Guidelines](#pull-request-guidelines)
5. [Style Guide](#style-guide)
6. [Questions or Feedback?](#questions-or-feedback)

---

## **Code of Conduct**
Before contributing, please read and adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). We are committed to fostering a welcoming and inclusive community for everyone.

---

## **How to Contribute**

### **Reporting Bugs**
If you find a bug in the project, please follow these steps:
1. **Check the Issues**: Search the [Issues](https://github.com/henrymbuguak/ai-chatbot-customer-support/issues) to see if the bug has already been reported.
2. **Create a New Issue**: If the bug hasn’t been reported, open a new issue with a clear and descriptive title.
3. **Provide Details**:
   - Describe the bug and how to reproduce it.
   - Include screenshots, error messages, or logs if applicable.
   - Specify your environment (e.g., OS, Python version).

### **Suggesting Enhancements**
Have an idea for a new feature or improvement? Here’s how to share it:
1. **Check the Issues**: Search the [Issues](https://github.com/henrymbuguak/ai-chatbot-customer-support/issues) to see if your idea has already been suggested.
2. **Create a New Issue**: If not, open a new issue with a clear and descriptive title.
3. **Explain Your Idea**:
   - Describe the feature or enhancement.
   - Explain why it would be valuable.
   - Provide examples or mockups if possible.

### **Submitting Code Changes**
To contribute code changes, follow these steps:
1. **Fork the Repository**: Click the **Fork** button on the [repository page](https://github.com/henrymbuguak/ai-chatbot-customer-support) to create your own copy.
2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/henrymbuguak/ai-chatbot-customer-support.git
   cd ai-chatbot-customer-support
   ```
3. **Create a New Branch**:
   ```bash
   git checkout -b your-branch-name
   ```
4. **Make Your Changes**: Write your code and ensure it follows the [Style Guide](#style-guide).
5. **Test Your Changes**: Run the tests to ensure your changes don’t break anything.
6. **Commit Your Changes**:
   ```bash
   git add .
   git commit -m "Your commit message"
   ```
7. **Push Your Changes**:
   ```bash
   git push origin your-branch-name
   ```
8. **Open a Pull Request**: Go to the [repository page](https://github.com/henrymbuguak/ai-chatbot-customer-support) and click **New Pull Request**. Provide a clear description of your changes and reference any related issues.

---

## **Setting Up the Project**
To set up the project locally, follow these steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/henrymbuguak/ai-chatbot-customer-support.git
   cd ai-chatbot-customer-support
   ```
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**:
   - Rename `.env_copy` to `.env`.
   - Add your Deepseek API key to the `.env` file:
     ```bash
     DEEPSEEK_API_KEY=your_api_key_here
     ```
5. **Run the Flask App**:
   ```bash
   python app.py
   ```

---

## **Pull Request Guidelines**
To ensure your pull request is reviewed and merged quickly, follow these guidelines:
- **Keep It Small**: Focus on one feature or bug fix per pull request.
- **Write Clear Commit Messages**: Use descriptive commit messages that explain what you changed and why.
- **Update Documentation**: If your changes affect the project’s functionality, update the relevant documentation (e.g., README, docs/).
- **Run Tests**: Ensure all tests pass before submitting your pull request.

---

## **Style Guide**
To maintain consistency across the codebase, please follow these guidelines:
- **Python**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- **Flask**: Use Flask’s best practices for routing and app structure.
- **Docstrings**: Include docstrings for all functions and classes.
- **Formatting**: Use consistent indentation (4 spaces) and avoid trailing whitespace.

---

## **Questions or Feedback?**
If you have any questions or need help, feel free to:
- Open an [Issue](https://github.com/henrymbuguak/ai-chatbot-customer-support/issues).
- Reach out via email: [Henry Mbugua](https://www.linkedin.com/in/henrymbugua/)

---

Thank you for contributing to the **AI-Powered Chatbot for Customer Support** project! Your efforts help make this project better for everyone. 🚀

