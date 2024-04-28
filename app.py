from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route and its corresponding view function
@app.route('/')
def hello_world():
    return 'Server is running up'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=8080)
