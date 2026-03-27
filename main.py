class Comment:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        self.vote_qty = 0
        Comment.total_comments += 1


first_comment = Comment("First comment")
print(Comment.total_comments)

Comment.total_comments = 10

print(Comment.total_comments)
print(first_comment.total_comments)
# first commit
