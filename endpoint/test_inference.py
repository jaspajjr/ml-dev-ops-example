from inference import process_request


def test_process_request():
    # arrange
    request_form = {'default': 100}

    # act
    result = process_request(request_form)

    # assert
    assert isinstance(result, dict)
    assert result.keys() == ['default']
    assert result.values() == [100]