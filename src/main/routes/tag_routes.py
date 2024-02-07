from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tag_routes_bp = Blueprint("tag_routes", __name__)

@tag_routes_bp.post("/create_tag")
def create_tag():

    tag_creator_view = TagCreatorView()

    http_request = HttpRequest(body=request.json)
    response = tag_creator_view.validate_and_create(http_request)
    
    return jsonify(response.body), response.status_code

# @tag_routes_bp.post("/other1")
# def other1():
#     ...

# @tag_routes_bp.post("/other2")
# def other2():
#     ...