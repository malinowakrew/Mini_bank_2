from datetime import datetime
import mongoengine

class Post(mongoengine.EmbeddedDocument):
    title = mongoengine.StringField(required=True, max_length=200)
    content = mongoengine.StringField(required=True)
    author = mongoengine.StringField(required=True, max_length=50)
    published = mongoengine.DateTimeField(default=datetime.datetime.now)