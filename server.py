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

class PlayerInsertHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def post(self):
		name = self.get_argument('name', '')
		num_group = self.get_argument('num_group', '')

		if not name:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите имя.'
			}
		elif not num_group:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите номер группы.'
			}
		else:
			response = {
				'error': False, 
				'msg': 'Спасибо.'
			}
			conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
			cur = conn.cursor()
			yield cur.execute("INSERT INTO players (name, num_group) VALUES (%s, %s)", (name, num_group, ))
			conn.commit()
			cur.close()
			conn.close()

		self.write(str(response))

class GameInsertHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def post(self):
		description = self.get_argument('description', '')
		name = self.get_argument('name', '')
		min_players = self.get_argument('min_players', '')
		min_players = self.get_argument('max_players', '')

		if not name:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите имя.'
			}
		elif not description:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите описание.'
			}
		elif not min_players:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите минимальное количество игроков.'
			}
		elif not max_players:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите максимальное количество игроков.'
			}
		else:
			response = {
				'error': False, 
				'msg': 'Спасибо.'
			}
			conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
			cur = conn.cursor()
			yield cur.execute("INSERT INTO players (description, name, min_players, max_players) VALUES (%s, %s, %s, %s)", 
				(name, num_group, min_players, max_players))
			conn.commit()
			cur.close()
			conn.close()

		self.write(str(response))

application = tornado.web.Application([
	(r"/select_games", GamesHandler), 
	(r"/select_events", EventsHandler),
	(r"/select_players", PlayersHandler),
	(r"/insert_player", PlayerInsertHandler)],
	debug = True
)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(80)
    tornado.ioloop.IOLoop.instance().start()
