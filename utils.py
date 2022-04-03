import json


def get_posts_all():
    posts = []
    with open('data/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in data:
            posts.append(i)
    return posts
    # except FileNotFoundError:
    #     # Будет выполнено, если файл не найден
    #     logging.error("Файл не найден")
    # except JSONDecodeError:
    #     # Будет выполнено, если файл найден, но не превращается из JSON
    #     logging.error("Файл не удается преобразовать")


def get_posts_by_user(user_name):
    posts = get_posts_all()
    users_posts = []
    for post in posts:
        if user_name.lower() == post['poster_name'].lower():
            users_posts.append(post)
    return users_posts


def get_comments_by_post_id(post_id):
    comments = []
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for comment in data:
            if post_id == comment['post_id']:
                comments.append(comment)
        return comments


def search_for_posts(query):
    data = get_posts_all()
    list_of_posts = []
    for post in data:
        if query.lower() in post['content'].lower():
            list_of_posts.append(post)
    return list_of_posts


def get_post_by_pk(pk):
    data = get_posts_all()
    for post in data:
        if pk == post['pk']:
            return post


def search_tags(tag):
    posts = get_posts_all()
    list_of_posts = []
    for post in posts:
        for i in post['tags']:
            if tag in i:
                list_of_posts.append(post)
    return list_of_posts


def load_bookmarks():
    with open('data/bookmarks.json', encoding='windows-1251') as file:
        data = json.load(file)
    return data


def add_bookmarks(path, data, new_data):
    if new_data not in data:
        data.append(new_data)
    else:
        for elem in data:
            if elem == new_data:
                data.remove(elem)
    with open(path, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)