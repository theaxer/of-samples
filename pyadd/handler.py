import json


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    try:
        data = json.loads(req)
    except:
        data = []

    return sum(data)
