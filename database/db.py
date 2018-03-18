import pymysql.cursors


def get_connection():
  return pymysql.connect(
    host='localhost',
    user='root',
    db='Andell',
    port=3306,
    autocommit=True,
    cursorclass=pymysql.cursors.DictCursor,
  )


def execute(query, values=None):
  conn = get_connection()
  try:
    # Create a cursor that can store query results
    with conn.cursor() as cursor:
      cursor.execute(query, values)
      return cursor.fetchall()
  finally:
    conn.close()
