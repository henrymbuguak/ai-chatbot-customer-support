def init_routes(app):
    @app.route('/')
    def home():
        return "Hello, GreenGrocer Foods!"