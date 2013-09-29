from bottle import route, run
@route('/')
@route('/greet/Jessie')

def index():
	return "Hello World!"
	
def greet(name):
	return "Hello, %s!" % name

if __name__ == '__main__':
	run(debug=True, reloader=True, host='0.0.0.0')