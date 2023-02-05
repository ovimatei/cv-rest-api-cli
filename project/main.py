from flask import Flask, jsonify, make_response
from json_data import personal_information, experience, education
from helpers import (
    build_education_string,
    build_experience_string,
    build_personal_information_string,
)

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/")
def hello():
    return """
    Hello! Available endpoints are:
    <ul>
    <li><a href='/personal'>/personal</a></li>
    <li><a href='/education'>/education</a></li>
    <li><a href='/experience'>/experience</a></li>
    </ul>
    """


@app.route("/personal", methods=["GET"])
def get_personal():
    return jsonify(personal_information)


@app.route("/experience", methods=["GET"])
def get_experience():
    return jsonify(experience)


@app.route("/education", methods=["GET"])
def get_education():
    return jsonify(education)


@app.cli.command("print_data")
def print_data():
    print("Personal Information:")
    build_personal_information_string(personal_information)
    print("Experience:")
    build_experience_string(experience)
    print("Education")
    build_education_string(education)
