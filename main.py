from graphene import ObjectType, Schema, String, ID, DateTime, List, Int
import json
from datetime import datetime

class User(ObjectType):

    id = ID()
    username = String()
    last_login = DateTime()

class Query(ObjectType):
    users = List(User, first = Int())

    def resolve_users(self, info, first):
        return[
            User(username='Omkar', last_login = datetime.now()),
            User(username='Kushal', last_login = datetime.now()),
            User(username='Parth', last_login = datetime.now()),
        ][:first]

schema = Schema(query = Query)

result = schema.execute(
    '''
    {
        users(first : 1) {
            username
            lastLogin
        }
    }
    '''
)

item = dict(result.data.items())
print(json.dumps(item, indent=4))
