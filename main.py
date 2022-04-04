from flask import Flask, render_template, request, redirect, jsonify
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user, search_tags, add_bookmarks, load_bookmarks


app = Flask(__name__)
path = 'data/bookmarks.json'

app.config.from_pyfile('config.py')


@app.route('/')
def main_page():
    posts = get_posts_all()
    bookmarks = load_bookmarks()
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@app.route('/posts/<int:postid>')
def show_post(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    return render_template('post.html', post=post, comments=comments, len_comments=len(comments))


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/search/results/')
def search_posts():
    s = request.args.get('s')
    list_of_posts = search_for_posts(s)
    return render_template('results.html', s=s, posts=list_of_posts, len=len(list_of_posts))


@app.route('/users/<user_name>')
def user_feed(user_name):
    users_posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=users_posts)


@app.route('/tags/<tag>')
def search_tags_of(tag):
    list_of_posts = search_tags(tag)
    return render_template('tag.html', posts=list_of_posts, tag=tag)


@app.route('/bookmarks/add/<int:postid>')
def add_to_bookmarks(postid):
    bookmark = request.args.get('bookmark')
    posts = load_bookmarks()
    post = get_post_by_pk(postid)
    add_bookmarks(path, posts, post)
    return redirect('/', code=302)


@app.route('/bookmarks')
def show_bookmarks():
    bookmarks = load_bookmarks()
    return render_template('bookmarks.html', posts=bookmarks)


@app.route('/api/posts')
def get_data():
    data = get_posts_all()
    return jsonify(data)


@app.route('/api/posts/<int:postid>')
def get_post(postid):
    post = get_post_by_pk(postid)
    return jsonify(post)


if __name__ == '__main__':
	app.run()
