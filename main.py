from bottle import route, run
from policy import Policy


@route('/urlinfo/1/<url:path>')
def geturls(url):
    policy = Policy(url)
    return policy.finde_in_db()

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)