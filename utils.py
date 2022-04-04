import json


def get_posts_all():
    """Получаем список постов из файла"""
    posts = []
    with open('data/data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in data:
            posts.append(i)
    return posts


def get_posts_by_user(user_name):
    """Получаем пост по имени"""
    posts = get_posts_all()
    users_posts = []
    for post in posts:
        if user_name.lower() == post['poster_name'].lower():
            users_posts.append(post)
    return users_posts


def get_comments_by_post_id(post_id):
    """Получаем список комментариев под необходимым постом"""
    comments = []
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for comment in data:
            if post_id == comment['post_id']:
                comments.append(comment)
        return comments


def search_for_posts(query):
    """Получаем список постов по вхождению слова"""
    data = get_posts_all()
    list_of_posts = []
    for post in data:
        if query.lower() in post['content'].lower():
            list_of_posts.append(post)
    return list_of_posts


def get_post_by_pk(pk):
    """Получаем пост по айди"""
    data = get_posts_all()
    for post in data:
        if pk == post['pk']:
            return post


def search_tags(tag):
    """Получаем список постов по тегам"""
    posts = get_posts_all()
    list_of_posts = []
    for post in posts:
        for i in post['tags']:
            if tag in i:
                list_of_posts.append(post)
    return list_of_posts


def load_bookmarks():
    """Получаем данные из файла"""
    with open('data/bookmarks.json', encoding='utf-8') as file:
        data = json.load(file)
    return data


def add_bookmarks(path, data, new_data):
    """Обновляем файл. Если нет поста в файле - добавляем, если есть - удаляем"""
    if new_data not in data:
        data.append(new_data)
    else:
        for post in data:
            if post == new_data:
                data.remove(post)
    with open(path, 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)