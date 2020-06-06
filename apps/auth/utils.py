from rest_framework_jwt.settings import api_settings


def jwt_encode(user):
    """
    Given a user, it creates a valid JWT token for it.
    """
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)
