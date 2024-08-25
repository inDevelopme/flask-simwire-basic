from . import app
from flask import Flask, jsonify, request, render_template

@app.route('/template_health_check')
def index():
    return render_template('template_health_check.html')

@app.route('/hello_world')
def hello_world():
    return 'Hello, World! This is my Flask application running on ECS.'

@app.route('/has_docker_compose_yml')
def has_dockerr_composer_yml():
    return 'Yes this image includes docker-compose.yml for building containers locally.'


# this makes sure that we exclude health checks in the SQL session management
@app.before_request
def exclude_health_check_routes():
    if request.path.startswith('/health_check'):
        try:
            return jsonify(status='ok')
        except (TypeError, ValueError) as e:
            # Handle any exceptions that may occur during the health check
            return jsonify(status='error', message='error'), 500  # Return a 500 Internal Server Error on failure

@app.route('/health_check')
def health_check():
    # Minimal health check logic here (e.g., check database connection)
    try:
        # Perform a minimal check (e.g., check the database connection)
        # If using SQLAlchemy, roll back any uncommitted transactions to avoid session creation
        return jsonify(status='ok')
    except (TypeError, ValueError) as e:
        # Handle any exceptions that may occur during the health check
        return jsonify(status='error', message='error'), 500  # Return a 500 Internal Server Error on failure
