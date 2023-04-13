import pytest

def test_render_template(client):
    response = client.get('templates')
    assert response.status_code == 200