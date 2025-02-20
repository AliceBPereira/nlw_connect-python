from cerberus import Validator

def events_creator_validator(rquest: any):
    body_validator = Validator({
        "data": {
            "type": "dict",
            "schema": {
                "name": {
                    "type": "string",
                    "required": True,
                    "empty": False
                }
            }
        }
    })

    response = body_validator.validate(rquest.json)

    if response is False:
        print(body_validator.errors)