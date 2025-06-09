from flask import Flask, request, current_app, g, make_response
import os

app = Flask(__name__)

@app.before_request
def app_path():
    # Store the absolute path of the current working directory in g.path
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    # Access Host header from the incoming HTTP request
    host = request.headers.get('Host')
    # Get the Flask application name
    appname = current_app.name
    # Get the stored path from the request context
    path = g.path

    # Create the HTML response body
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {path}</h3>
    '''

    # Return the response with status code 200 OK
    return make_response(response_body, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
