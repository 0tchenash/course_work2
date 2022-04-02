from flask import Flask, render_template, send_from_directory, request
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts, get_posts_by_user, search_tags

app = Flask(__name__)


@app.route('/')
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


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


app.run(debug=True)
