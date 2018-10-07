import requests as r

def login():

    data = {
        "grant_type": "password",
        "client_id": "c82SH0WZOsabOXGP2sxqcj34FxkvfnWRZBKlBjFS",
        "password": "PASSWORD",
        "username": "USERNAME"
    }

    url = "https://api.robinhood.com/oauth2/token/"

    res = r.post(url, data=data)

    print(res)


if __name__ == "__main__":
    login()
