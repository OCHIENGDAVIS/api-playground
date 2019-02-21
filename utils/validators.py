from app.v1.models import offices

def validate_json(json_input):
    if not json_input:
        return False
    return True



def validate_id(_id):
    if not isinstance(_id, int):
        return False
    return True


def validate_empty_string(string_input):
    if not isinstance(string_input, str) or string_input == "":
        return  False
    return True


def validate_keys_exists(data):
    required_keys = ['id', 'name', 'type']
    for key in required_keys:
        if key not in list(data.keys()):
            return False
    return True



