from bottle import route, run, HTTPResponse
import requests
import os

@route('/')
def index():
    return(f'<h2>Main page</h2><hr>')

@route('/success')
def success():
    resp = HTTPResponse().status_code
    return(f'<h2>Success page</h2><hr></br>Status: {resp}')

@route('/fail')
def fail():
    fail()
    return HTTPResponse(status=500, body="Fail page")

def main():
    run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    

if __name__ == "__main__":
    main()