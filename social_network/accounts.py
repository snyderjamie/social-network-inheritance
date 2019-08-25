class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.posts = []
        self.following = []

    def add_post(self, post):
        post.set_user(self)
        self.posts.append(post)
    
    def get_timeline(self):
        results = []
        for user in self.following:
            results += user.posts
        return sorted(results, key=lambda x: x.timestamp, reverse=False)
#         return result.sort(key=lambda x: getattr(x, self.posts.timestamp), reverse=False) 

    def follow(self, other):
        return self.following.append(other)
