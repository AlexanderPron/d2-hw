from bottle import route, run
import requests

@route('/')
def index():
    return(f'<h2>Main page</h2><hr>')

@route('/fail')
def fail():
    return(f'<h2>FAilpage</h2><hr>')

def main():
    run(host='0.0.0.0', port=8080)
    

if __name__ == "__main__":
    main()