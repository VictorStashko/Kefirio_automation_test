GET = {
    "list_users": "/api/users?page=2",
    "single_user": "/api/users/2",
    "not_found": "/api/users/23"
}

POST = {
    "create": {
        "url": "/api/users",
        "body": {"name": "morpheus", "job": "leader"}
    },
    "register_successful": {
        "url": "/api/register",
        "body": {"email": "eve.holt@reqres.in", "password": "pistol"}
    },
}

PUT = {
    "update": {
        "url": "/api/users/2",
        "body": {"name": "morpheus", "job": "zion resident"}
    }
}
