from graphene import ObjectType, Schema, String, ID, DateTime, List, Int, Mutation
import json
from datetime import datetime

from graphene.types.field import Field

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

class CreateUser(Mutation):
    class Arguments:
        username = String()

    user = Field(User)

    def mutate(self, info, username):
        if info.context.get('is_vip'):
            username = username.upper()
        user = User(username=username)
        return CreateUser(user=user)

class Mutations(ObjectType):
    create_user = CreateUser.Field()

schema = Schema(query = Query, mutation= Mutations)

result = schema.execute(
    '''
    mutation createUserMutation($username : String) {
        createUser(username: $username){
            user {
                username
            }
        }
    }
    ''',
    variable_values = {"username" : "Bob"},
    context = {"is_vip" : False}
)

item = dict(result.data.items())
print(json.dumps(item, indent=4))
