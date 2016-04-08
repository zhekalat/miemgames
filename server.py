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
		result = []
		for row in cur:
			result.append({'name': str(row[2]), 'min_players': str(row[3]), 'max_players':  str(row[4]), 'description': str(row[1])})
		self.write({"games": result})
		cur.close()
		conn.close()

class EventsHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
		cur = conn.cursor()
		yield cur.execute("SELECT * FROM events")
		result = []
		for row in cur:
			result.append({'game': str(row[1]), 'time': str(row[2]), 'place': str(row[3])})
		self.write({"events": result})
		cur.close()
		conn.close()

class PlayersHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
		cur = conn.cursor()
		yield cur.execute("SELECT * FROM players")
		result = []
		for row in cur:
			result.append({'name': str(row[1]), 'num_group': str(row[2]), 'rating': str(row[3])})
		self.write({"players":result})
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
			try:
				conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
				cur = conn.cursor()
				yield cur.execute("INSERT INTO players (name, num_group) VALUES (%s, %s)", (name, num_group, ))
				yield cur.execute("SELECT id FROM players WHERE name = %s AND num_group = %s", (name, num_group[: 6], ))
				conn.commit()
				id_ = str(cur.fetchone()[0])
				cur.close()
				conn.close()
				response = {
					'error' : False,
					'id' : id_
				}
			except:
				response = {
					'error': True,
					'msg': 'double value'
				}
		self.write(response)

class GameInsertHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def post(self):
		name = self.get_argument('name', '')
		description = self.get_argument('description', '')
		min_players = self.get_argument('min_players', '')
		max_players = self.get_argument('max_players', '')

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
			try:
				conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
				cur = conn.cursor()
				yield cur.execute("INSERT INTO games (description, name, min_players, max_players) VALUES (%s, %s, %s, %s)", 
					(description, name, min_players, max_players))			
				yield cur.execute("SELECT id FROM games WHERE description = %s AND name = %s AND min_players = %s  AND max_players = %s", 
					(description, name, min_players, max_players))
				conn.commit()
				id_ = str(cur.fetchone()[0])
				cur.close()
				conn.close()
				response = {
					'error': False,
					'id': id_
				}
			except:
				response = {
					'error' : True,
					'msg' : 'double value'
				}
		self.write(response)

class EventInsertHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def post(self):
		game = self.get_argument('game', '')
		time = self.get_argument('time', '')
		place = self.get_argument('place', '')

		if not game:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите id игры.'
			}
		elif not time:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите время.'
			}
		elif not place:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите место.'
			}
		else:
			try:
				conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
				cur = conn.cursor()
				yield cur.execute("INSERT INTO events (game, time, place) VALUES (%s, %s, %s)", 
					(game, time, place))			
				yield cur.execute("SELECT id FROM events WHERE game = %s AND time = %s AND place = %s", 
					(game, time, place))
				conn.commit()
				id_ = str(cur.fetchone()[0])
				cur.close()
				conn.close()
				response = {
					'error': False,
					'id': id_
				}
			except:
				response = {
					'error' : True,
					'msg' : 'double value'
				}	
		self.write(response)

class ParticipantInsertHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def post(self):
		player = self.get_argument('player', '')
		event = self.get_argument('event', '')

		if not player:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите id игрока.'
			}
		elif not event:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите id события.'
			}
		else:
			try:
				conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
				cur = conn.cursor()
				yield cur.execute("INSERT INTO participants (event, player) VALUES (%s, %s)", 
					(event, player))
				conn.commit()
				cur.close()
				conn.close()
				response = {
					'error': False
				}
			except:
				response = {
					'error' : True,
					'msg' : 'double value'
				}	
		self.write(response)

class PlayersFromParticipantsHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def post(self):
		player = self.get_argument('player', '')

		if not player:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите id игрока.'
			}
		else:
			try:
				conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
				cur = conn.cursor()
				yield cur.execute("SELECT e.id, g.name, e.time, e.place FROM players p, participants pa, events e, games g WHERE pa.player = p.id AND g.id = e.game AND e.id = pa.event AND p.id = %s", 
					(player))
				response = []
				for i, row in enumerate(cur):
					response.append({'id': str(row[0]), 'name': str(row[1]), 'time': str(row[2]), 'place': str(row[3])})
				response = {"payers": response}
				cur.close()
				conn.close()
			except:
				response = {
					'error' : True,
					'msg' : 'Данный игрок не учавствует ни в каких играх.'
				}	
		self.write(response)

class EventsFromParticipantsHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def post(self):
		event = self.get_argument('event', '')

		if not event:
			response = {
				'error': True, 
				'msg': 'Пожалуйста, введите id события.'
			}
		else:
			try:
				conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
				cur = conn.cursor()
				yield cur.execute("SELECT p.* FROM players p, participants pa, events e, games g WHERE pa.player = p.id AND g.id = e.game AND e.id = pa.event AND e.id = %s", 
					(event))
				response = []
				for i, row in enumerate(cur):
					response.append({'id': str(row[0]), 'name': str(row[1]), 'num_group': str(row[2]), 'rating': str(row[3])})
				response = {"events": response}
				cur.close()
				conn.close()
			except:
				response = {
					'error' : True,
					'msg' : 'Данного события не существует.'
				}	
		self.write(response)

class GamesPicHandler(tornado.web.RequestHandler):
	@gen.coroutine
	def get(self):
		conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
		cur = conn.cursor()
		yield cur.execute("SELECT name, description, picture FROM games")
		result = []
		for row in cur:
			result.append({'name': str(row[0]), 'description': str(row[1]), 'picture':  str(row[2])})
		self.write({"games": result})
		cur.close()
		conn.close()

application = tornado.web.Application([
	(r"/select_games", GamesHandler), 
	(r"/select_events", EventsHandler),
	(r"/select_players", PlayersHandler),
	(r"/insert_player", PlayerInsertHandler),
	(r"/insert_game", GameInsertHandler),
	(r"/insert_event", EventInsertHandler),
	(r"/insert_participant", ParticipantInsertHandler),
	(r'/select_players_from_participants', PlayersFromParticipantsHandler),
	(r'/select_events_from_participants', EventsFromParticipantsHandler),
	(r'/select_games_with_picture', GamesPicHandler)],
	debug = True
)

if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(255)
	tornado.ioloop.IOLoop.instance().start()
