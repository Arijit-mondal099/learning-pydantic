from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    user_id: int
    content: str
    replies: Optional[List[Comment]] = None

Comment.model_rebuild()

comments = Comment(
    id=1,
    user_id=2,
    content="hi",
    replies=[
        Comment(id=2, user_id=1, content="hello", replies=[Comment(id=4, user_id=2, content="bye")]),
        Comment(id=3, user_id=5, content="hello"),
    ]
)

print(comments.model_dump())
