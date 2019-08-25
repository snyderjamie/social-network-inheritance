from datetime import datetime

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp.strftime("%A, %b %d, %Y")
        self.user = None

    def set_user(self, user):
        self.user = user
        

class TextPost(Post):
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        result = '@{fname} {lname}: "{text}"\n\t{date}'.format(fname=self.user.first_name, lname=self.user.last_name, text=self.text, date=self.timestamp)
        return result
    

class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=None):
        PicturePost.image_url = image_url
        super(PicturePost, self).__init__(text, timestamp)
        
    def __str__(self):
        result = '@{fname} {lname}: "{text}"\n\t{url}\n\t{date}'.format(
                fname=self.user.first_name, lname=self.user.last_name, text=self.text, url=self.image_url, date=self.timestamp)
        return result


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=None):
        CheckInPost.latitude = latitude
        CheckInPost.longitude = longitude
        super(CheckInPost, self).__init__(text, timestamp)

    def __str__(self):
        result = '@{fname} Checked In: "{text}"\n\t{lat}, {lon}\n\t{date}'.format(fname=self.user.first_name, text=self.text, lat=self.latitude, lon=self.longitude, date=self.timestamp)
        return result