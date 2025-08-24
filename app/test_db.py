import mysql.connector

def get_db_connection(phost,puser,ppassword,pdatabase):
  try:
    conn = mysql.connector.connect(host=phost,user=puser,password=ppassword,database=pdatabase)
    return conn
  except mysql.connector.Error as err:
    print(f"Error: {err}")
    return None

def get_data(pconn,pquery):
  try:
    cursor =pconn.cursor()
    cursor.execute(pquery)
    results= cursor.fetchall()
    return results
  except mysql.connector.Error as err:
    print(f"Error: {err}")
    return None
  finally:
    if conn:
      conn.close()

def get_databases(pconn):
  try:
    cursor = pconn.cursor()
    cursor.execute("SHOW DATABASES")
    results = cursor.fetchall()
    return results
  except mysql.connector.Error as err:
    print(f"Error: {err}")
    return None
  finally:
    if conn:
      conn.close()
print("start")
conn=get_db_connection("103.86.177.4","kbnhzraf_retail","Inspire123$","kbnhzraf_ticketdb")
print(conn)
print("2nd")
results =get_data(conn,"SELECT * FROM tblcustomer")
print(results)
print("3")

conn=get_db_connection("103.86.177.4","kbnhzraf_retail","Inspire123$","kbnhzraf_ticketdb")
results =get_databases(conn)
print(results)
print("final")
