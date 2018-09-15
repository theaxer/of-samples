import json


def handle(req):
    """handle a request to add the input
    Args:
        req (str): request body
    """

    try:
        data = json.loads(req)
    except:
        data = []

    try:
        return sum(data)
    except Exception as e:
        return str(e)
