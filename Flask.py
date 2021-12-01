from flask import Flask, request
from graphene import ObjectType, String, Schema
import json

app = Flask(__name__)

class Query(ObjectType):
        hello = String(name = String(default_value="World"))

        def resolve_hello(self, info, name):
            return 'Hello ' + name

schema = Schema(query = Query)

@app.route('/graphql', methods=["POST"])
def graphql():
    data = json.loads(request.data)
    return json.dumps(schema.execute(data["query"]).data) #body : {  "query" : "{ hello( name :\"Omkar\") }" }
    


if __name__ == "__main__":
    app.run(debug=True)