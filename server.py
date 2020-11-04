from bottle import route, run
import requests
import os

@route('/')
def index():
    return(f'<h2>Main page</h2><hr>')

@route('/fail')
def fail():
    return(f'<h2>FAilpage</h2><hr>')

def main():
    run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    

if __name__ == "__main__":
    main()