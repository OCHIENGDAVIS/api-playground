
from flask import Blueprint, jsonify, request
from app.v1.models import Office
from app.v1.models import Party
from utils.validators import validate_empty_string, validate_id, validate_json
from utils.helpers import custom_response

office= Blueprint("office", __name__)
party = Blueprint("party", __name__)


@office.route("/offices", methods = ["GET"])
def get_all_offices():
    offices = Office.get_all_offices()
    return  jsonify({
        "status": 200,
        "data": offices
    })


@office.route("/offices", methods=["POST"])
def create_office():
    user_input = request.get_json()
    data = validate_json(request.get_json())
    _id = validate_id(user_input.get("id"))
    name = validate_empty_string(user_input.get("name"))
    _type = validate_empty_string(user_input.get("type"))
    exists = Office.office_does_not_exists(user_input.get("id"))
    valid_keys = [data, _id, name, _type, exists]
    for key in valid_keys:
        if not key:
            response = custom_response(400, f"Invalid Input! check on data you are trying to submit")
            return response
    new_office = Office.save_office(user_input.get("id"), user_input.get("name"), user_input.get("type"))
    return jsonify({
        "status": 201,
        "data": [{
            "id":new_office["id"],
            "name": new_office["name"]
        }]
    })


@party.route("/parties", methods = ["GET"])
def get_all_parties():
    parties = Party.get_all_parties()
    return  jsonify({
        "status": 200,
        "data": parties
    })





@party.route("/parties", methods=["POST"])
def create_party():
    user_input = request.get_json()
    data = validate_json(request.get_json())
    _id = validate_id(user_input.get("id"))
    name = validate_empty_string(user_input.get("name"))
    hqAddress = validate_empty_string(user_input.get("hqAddress"))
    logoUrl = validate_empty_string(user_input.get("logoUrl"))
    exists = Party.party_does_not_exists(user_input.get("id"))
    valid_keys = [data, _id, name, logoUrl, hqAddress, exists]
    for key in valid_keys:
        if not key:
            response = custom_response(400, f"Invalid Input! check on data you are trying to submit")
            return response
    new_party = Party.save_party(user_input.get("id"), user_input.get("name"), user_input.get("hqAddress"), user_input.get("logoUrl"))
    return jsonify({
        "status": 201,
        "data": [{
            "id":new_party["id"],
            "name": new_party["name"]
        }]
    })


@party.route("/offices/<int:office_id>", methods=["GET"])
def get_an_office(office_id):
    office_found= Office.get_an_office_by_id(office_id)
    if office_found is not False:
        return jsonify({
            "status": 200,
            "data": [{
                "id":office_found["id"],
                "name": office_found["name"]
            }]
        })
    return jsonify({
        "status": 404,
        "data":[{
            "message": "Office does not exists"
        }]
    }), 404



@party.route("/parties/<int:party_id>", methods=["GET"])
def get_a_party(party_id):
    party_found= Party.get_a_party_by_id(party_id)
    if party_found is not False:
        return jsonify({
            "status": 200,
            "data": [{
                "id":party_found["id"],
                "name": party_found["name"]
            }]
        })
    return jsonify({
        "status": 404,
        "data":[{
            "message": "Party does not exists"
        }]
    }), 404

@party.route("/parties/<int:party_id>/name", methods=["PATCH"])
def patch_a_party(party_id):
    user_input = request.get_json()
    data = validate_json(request.get_json())
    name = validate_empty_string(user_input.get("name"))
    valid_keys = [data, name]
    for key in valid_keys:
        if not key:
            response = custom_response(400, f"Invalid Input! check on data you are trying to submit")
            return response
    party_patched= Party.patch_a_party(party_id, user_input.get("name"))
    if party_patched is not False:
        return jsonify({
            "status": 200,
            "data": [{
                "id":party_patched["id"],
                "name": party_patched["name"]
            }]
        })
    return jsonify({
        "status": 404,
        "data":[{
            "message": "Party does not exists"
        }]
    }), 404

@party.route("/parties/<int:party_id>", methods=["DELETE"])
def delete_a_party(party_id):
    party_delete= Party.delete_a_party(party_id)
    if party_delete is not False:
        return jsonify({
            "status": 200,
            "data": [{
                "message": "Party deleted successfully"
            }]
        })
    return jsonify({
        "status": 404,
        "data":[{
            "message": "Party does not exists"
        }]
    }), 400
