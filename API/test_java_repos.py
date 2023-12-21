from java_repos import api_call

def test_api_call():
    r = api_call()
    status = r.status_code
    assert status == 200
