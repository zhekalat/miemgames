import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen as gen
import tornado_mysql
import json 

class GamesHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
		cur = conn.cursor()
		yield cur.execute("SELECT * FROM games")
		result = {}
		for i, row in enumerate(cur):
			result[i] = {'name': str(row[2]), 'min_players': str(row[3]), 'max_players':  str(row[4]), 'description': str(row[1])}
		self.write(str(result))
		cur.close()
		conn.close()

class EventsHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
		cur = conn.cursor()
		yield cur.execute("SELECT * FROM events")
		result = {}
		for i, row in enumerate(cur):
			result[i] = {'game': str(row[2]), 'title': str(row[3]), 'place': str(row[4])}
		self.write(str(result))
		cur.close()
		conn.close()

class PlayersHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
		cur = conn.cursor()
		yield cur.execute("SELECT * FROM players")
		result = {}
		for i, row in enumerate(cur):
			result[i] = {'name': str(row[2]), 'num_group': str(row[3]), 'rating': str(row[4])}
		self.write(str(result))
		cur.close()
		conn.close()

application = tornado.web.Application(
	[(r"/select_games", GamesHandler)],
	[(r"/select_events", EventsHandler)],
	[(r"/select_players", PlayersHandler)],
	debug = True
)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(80)
    tornado.ioloop.IOLoop.instance().start()
