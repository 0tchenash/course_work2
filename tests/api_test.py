from main import app


def test_post():

	allowed_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk", "tags"}
	response = app.test_client().get('/api/posts/3')
	fact_keys = set(response.json.keys())

	assert fact_keys == allowed_keys, 'Wrong keys'
	assert response.json.get('pk') == 3, 'Wrong post ID'


def test_posts():

	response = app.test_client().get('/api/posts')
	allowed_keys = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk", "tags"}

	assert response.status_code == 200, 'Wrong status-code'
	assert len(response.json) > 0, 'Data list is empty'
	for elem in response.json:
		fact_keys = set(elem.keys())
		assert fact_keys == allowed_keys, 'Wrong keys'