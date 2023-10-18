import mongoengine as mongo


class User(mongo.Document):
    email = mongo.StringField(required=True)
    first_name = mongo.StringField(max_length=50)
    last_name = mongo.StringField(max_length=50)

# class Post(mongo.document):
