import pymysql.cursors

def select_games():
	result = {} 

	connection = pymysql.connect(host = 'localhost',
								 user = 'galayko',
								 password = '',
								 db = 'miemgame',
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

print(select_games()[0])