import requests
import json

# Endpoint URL
url = 'http://127.0.0.1:5000/graphql'

# GraphQL query
query = '''
{
  allParts {
    edges {
      node {
        id
        name
        category
        compatibleWith
      }
    }
  }
}
'''

def test_all_parts_query():
    response = requests.post(url, json={'query': query})
    if response.status_code == 200:
        print("Query successful!")
        data = response.json()
        print(json.dumps(data, indent=2))
    else:
        print("Query failed!")
        print("Status code:", response.status_code)
        print("Response:", response.text)

if __name__ == '__main__':
    test_all_parts_query()
