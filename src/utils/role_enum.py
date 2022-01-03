import enum

@enum.unique
class Roles(enum.Enum):
    admin = "admin"
    member = "member"
    author = "author"