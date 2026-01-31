from db import get_connection

def main():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM users;")
    count = cur.fetchone()[0]

    print("Number of users in database:", count)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
