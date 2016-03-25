import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado_mysql

def insert_player(name, group):
	connection = pymysql.connect(host = 'localhost',
								 user = 'ubuntu',
								 password = '',
								 db = 'miemgames',
								 charset = 'utf8',
								 cursorclass = pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			sql = "insert into players (name, group) values (%s, %s);"
			cursor.execute(sql, (name, group))
			connection.commit()
	finally:
		connection.close()

def insert_event(game, time, place):
	connection = pymysql.connect(host = 'localhost',
								 user = 'ubuntu',
								 password = '',
								 db = 'miemgames',
								 charset = 'utf8',
								 cursorclass = pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			sql = "insert into players (game, time, place) values (%s, %s, %s);"
			cursor.execute(sql, (game, time, place))
			connection.commit()
	finally:
		connection.close()

def insert_game(name, description, min_players, max_players):
	connection = pymysql.connect(host = 'localhost',
								 user = 'ubuntu',
								 password = '',
								 db = '',
								 charset = 'utf8',
								 cursorclass = pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			sql = "insert into players (name, description, min_players, max_players) values (%s, %s, %d, %d);"
			cursor.execute(sql, (name, description, min_players, max_players))
			connection.commit()
	finally:
		connection.close()

def insert_participant(event, player):
	connection = pymysql.connect(host = 'localhost',
								 user = 'ubuntu',
								 password = '',
								 db = 'miemgames',
								 charset = 'utf8',
								 cursorclass = pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			sql = "insert into players (event, player) values (%d, %d);"
			cursor.execute(sql, (event, player))
			connection.commit()
	finally:
		connection.close()

def select_games():
	result = {} 

	connection = pymysql.connect(host = 'localhost',
								 user = 'ubuntu',
								 password = '',
								 db = 'miemgames',
								 charset = 'utf8',
								 cursorclass = pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as cursor:
			sql = "select * from games;"
			cursor.execute(sql)
			result = cursor.fetchall()
	finally:
		connection.close()

	return result

@gen.coroutine
def main():
    conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='ubuntu', passwd='', db='miemgames', charset='utf8')
    cur = conn.cursor()
    yield cur.execute("SELECT name FROM games")
    print(cur.description)
    for row in cur:
       print(row)
    cur.close()
    conn.close()

class GameHandler(tornado.web.RequestHandler):
    def get(self):
	ioloop.IOLoop.current().run_sync(main)
        #db = database.Connection("localhost", "miemgames", user = "ubuntu")
        #for game in d.query("SELECT * FROM games"):
        #        print(game)

        #for game in select_games():
        #	self.write(game)

application = tornado.web.Application(
	[(r"/select_games", GameHandler)],
	debug = True
)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(80)
    tornado.ioloop.IOLoop.instance().start()
