import mysql.connector
import os
from utils import logger

# Load environment variables

print("DB_HOST: ",os.getenv("DB_HOST"))
# ==========================
# Database Connection
# ==========================

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="103.86.177.4",#os.getenv("DB_HOST"),
            user="kbnhzraf_retail",#os.getenv("DB_USER"),
            password="Inspire123$",#os.getenv("DB_PASSWORD"),
            database="kbnhzraf_ticketdb"#os.getenv("DB_NAME")
            ,use_pure=True
        )
        logger.info("Database connection established")
        return conn
    except Exception as e:
        logger.error(f"Error connecting to database: {e}")
        raise

# ==========================
# Insert Leave Method
# ==========================
def insert_leave(description: str,empname: str, date: str,leave_id: int):
    conn = None
    cursor = None
    try:
        conn=get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
             "INSERT INTO leaves_tnx (description, empname, date, leave_id) VALUES (%s, %s, %s, %s)",
            (description, empname, date, leave_id)
        )
        conn.commit()
        logger.info(f"Inserted leave: {description}, {empname}, {date}, leave={leave_id}")
        return True
    except Exception as e:
        logger.error(f"Error inserting leave: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# ==========================
# Get All leave types Methods
# ==========================
def get_leave_types():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor=conn.cursor(dictionary=True)
        print(cursor)
        cursor.execute("SELECT * FROM leave_categories ORDER BY name ASC")
        rows = cursor.fetchall()
        print(rows)
        logger.info(f"Fetched {len(rows)} leaves")
        return rows
    except Exception as e:
        logger.error(f"Error fetching leave: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":

    #Insert Method
    insert_leave("Travel to hometown","Arun",'2025-08-20',1)
    print("Record Inserted")

    #get_leave_types Method
    records = get_leave_types()
    print(records)

   