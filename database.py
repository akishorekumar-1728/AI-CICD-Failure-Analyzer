import sqlite3

DB_NAME = "failures.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS failures(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        repo TEXT,

        workflow TEXT,

        status TEXT,

        time TEXT,

        error TEXT

    )
    """)

    conn.commit()
    conn.close()


def insert_failure(repo, workflow, status, time, error):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO failures
        (repo,workflow,status,time,error)

        VALUES(?,?,?,?,?)
        """,

        (repo, workflow, status, time, error)

    )

    conn.commit()

    conn.close()


def get_failures():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT repo,workflow,status,time,error

        FROM failures

        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    failures = []

    for row in rows:

        failures.append({

            "repo": row[0],

            "workflow": row[1],

            "status": row[2],

            "time": row[3],

            "error": row[4]

        })

    return failures
def search_failures(search):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT repo, workflow, status, time, error
        FROM failures
        WHERE LOWER(repo) LIKE ?
        ORDER BY id DESC
    """, ('%' + search.lower() + '%',))

    rows = cursor.fetchall()

    conn.close()

    failures = []

    for row in rows:
        failures.append({
            "repo": row[0],
            "workflow": row[1],
            "status": row[2],
            "time": row[3],
            "error": row[4]
        })

    return failures