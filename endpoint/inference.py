def process_request(request_):
    '''
    Process the request to make a prediction.
    '''
    return {k: v for (k, v) in request_.items()}