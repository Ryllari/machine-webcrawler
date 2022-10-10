def mock_requests_get(*args, **kwargs):
    """
    Mock python requests.get behavior
    Avoiding made real requests on tests
    """
    class MockResponse:
        def __init__(self, status_code, file_text, reponse_ok=True):
            self.status_code = status_code
            self.text = file_text
            self.ok = reponse_ok

    filename = 'vultr.html'

    with open(f'tests/files/{filename}', 'r') as f:
        content_file = f.read()
        return MockResponse(200, content_file)