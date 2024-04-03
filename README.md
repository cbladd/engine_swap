# Engine Swap API

The Engine Swap API is an educational project that shows how to build a system for keeping track of car engine parts using Flask (a Python web framework) and GraphQL (a powerful query language for APIs), Python, SQLAlchemy, and Docker, this project is great for greasemonkeys and tech learners. 

## Features

- **GraphQL API**: Offers a flexible query language for your data, making it easy to fetch the exact information you need.
- **Engine Parts Management**: Add, query, and manage parts along with their compatibility information.
- **Docker Integration**: Ensures easy setup and deployment, encapsulating the application and its environment.
- **Database Support**: Utilizes MySQL for reliable storage and quick retrieval of engine parts data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose
- Python 3.8 or newer

### Installation

1. Clone the repository to your local machine:
git clone https://github.com/cbladd/engine-swap.git

2. Navigate to the project directory:
cd engine-swap

3. Build and start the services using Docker Compose:
docker-compose up --build


The API will be available at `http://127.0.0.1:5000/graphql`, where you can execute queries and mutations using the GraphiQL interface.

## Running the Tests

To ensure everything is set up correctly, you can run the provided test script:
python test_api.py

You should see a response like this:
$ python test_api.py 
Query successful!
{
  "data": {
    "allParts": {
      "edges": [
        {
          "node": {
            "id": "UGFydDox",
            "name": "Subaru EJ22 Engine",
            "category": "engine",
            "compatibleWith": "VW Vanagon"
          }
        },
        {
          "node": {
            "id": "UGFydDoy",
            "name": "Engine Conversion Kit",
            "category": "conversion kit",
            "compatibleWith": "VW Vanagon"
          }
        },
        {
          "node": {
            "id": "UGFydDoz",
            "name": "High Performance Exhaust",
            "category": "exhaust",
            "compatibleWith": "Subaru EJ22"
          }
        },
        {
          "node": {
            "id": "UGFydDo0",
            "name": "Transmission Adapter Plate",
            "category": "transmission",
            "compatibleWith": "VW Vanagon"
          }
        },
        {
          "node": {
            "id": "UGFydDo1",
            "name": "Upgraded Cooling System",
            "category": "cooling",
            "compatibleWith": "Subaru EJ22"
          }
        }
      ]
    }
  }
}

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [GraphQL](https://graphql.org/) - A query language for your API
- [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL toolkit and Object-Relational Mapper
- [Docker](https://www.docker.com/) - Containerization platform

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- **C.B. Ladd** - *Initial work* - [cbladd](https://github.com/cbladd)

See also the list of [contributors](https://github.com/cbladd/engine-swap/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

This project stands on the shoulders of many incredible open-source projects and contributions. We'd like to express our gratitude to the developers and communities behind the following technologies and libraries, without which the Engine Swap API would not have been possible:

- **[Flask](https://flask.palletsprojects.com/en/2.0.x/)**: A lightweight WSGI web application framework that serves as the backbone of our API.
- **[Werkzeug](https://werkzeug.palletsprojects.com/)**: A comprehensive WSGI web application library that Flask is built upon.
- **[Graphene](https://graphene-python.org/)**: A Python library for building GraphQL APIs in Python easily, its simplicity and flexibility being key to our project's quick development.
- **[Graphene-SQLAlchemy](https://github.com/graphql-python/graphene-sqlalchemy)**: An integration for Graphene to work with SQLAlchemy, which made it straightforward to expose our database models as GraphQL objects.
- **[Flask-GraphQL](https://github.com/graphql-python/flask-graphql)**: A Flask extension that adds GraphQL support to our Flask application, making it easier to create and expose GraphQL endpoints.
- **[Promise](https://github.com/syrusakbary/promise)**: A Promises/A+ implementation for Python that Graphene uses to handle asynchronous tasks.
- **[PyMySQL](https://pymysql.readthedocs.io/)**: A pure-Python MySQL client library that allowed us to interface seamlessly with our MySQL database.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: The Python SQL toolkit and Object-Relational Mapping (ORM) library that provided the full power and flexibility of SQL to our application.
- **[graphql-core](https://github.com/graphql-python/graphql-core)**: A Python port of GraphQL.js, the JavaScript reference implementation for GraphQL, which forms the core of our GraphQL service.

Thanks go to all the individual contributors and maintainers of these projects. 
