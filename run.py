from app import CONFIG
from app import app

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=CONFIG['PORT'], use_reloader=True, debug=CONFIG['DEBUG'])
