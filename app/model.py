
import json
class Post():
    def __init__(self,  title, image, summary, post, author, author_id):
        self.summary = summary
        self.image = image
        self.post = post
        self.title = title
        self.author = author
        self.author_id = author_id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)



# class PitchSchema(ma.Schema):
#     class Meta:
#         fields = ('id', 'title', 'description', 'summary', 'posted')