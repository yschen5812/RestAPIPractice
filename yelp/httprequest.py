import requests
import tokencache

token = tokencache.Authorization().getToken()

# Search API URL
searchUrl = 'https://api.yelp.com/v3/businesses/search'
# Add Other URLs


UrlTable = {
    'search': searchUrl
    # add more request types here
}


def sendRequest(requestType, payload):
    """
    Send request to ping Yelp API with provided payload

    Args:
        requestType(string): should be one of the keys in the UrlTable.
        paylaod(dict): the payload for the request.

    Returns:
        return a json format response.

    Raises:
        KeyError: raise this error if request type not supported.

    """
    if UrlTable.has_key(requestType):
        r = requests.get(searchUrl, headers=token, params=payload)
        print r.json()
    else:
        msg = "Error: unsupported requestType='{t}'".format(t=requestType)
        raise KeyError(msg);


## Sample
#payload = { 'term': 'Restaurant Week',
#            'location': 'ny',
#            'sort_by': 'rating' }
#
#sendRequest(requestType="search", payload=payload)
