import requests
import os
import sentry_sdk
from sentry_sdk.integrations.bottle import BottleIntegration
from bottle import route, run, HTTPResponse
from userconf import USER_DSN


@route('/')
def index():
    return(f'<h2>Main page</h2><hr>')

@route('/success')
def success():
    resp = HTTPResponse().status_code
    return(f'<h2>Success page</h2><hr></br>Status: {resp}')

@route('/fail')
def fail():
    raise RuntimeError

def main():
    sentry_sdk.init(
    dsn=USER_DSN,
    integrations=[BottleIntegration()]
    )
    run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


if __name__ == "__main__":
    main()