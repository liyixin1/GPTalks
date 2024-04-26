from mysql.connector import DatabaseError

import config


def insert_date(username, hashed, avatar):
    con = config.database.get_connection()
    cur = con.cursor()
    cur.execute("INSERT INTO users (username, password_hash, avatar) VALUES (%s, %s, %s)", (username, hashed, avatar))
    con.commit()
    config.database.close_connection(con, cur)


def select_date(username):
    con = config.database.get_connection()
    cur = con.cursor()
    cur.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    config.database.close_connection(con, cur)
    print("查询：", user[0])
    return user


def select_one_date(value, table, condition, condition_data):
    # value->目标, table->表, condition->条件, condition_data->条件值
    con = config.database.get_connection()
    cur = con.cursor()
    try:
        sql = "SELECT {} FROM {} WHERE {} = %s".format(value, table, condition)
        cur.execute(sql, (condition_data,))
        data = cur.fetchone()
        if data:
            print("select OK")
            return data[0]
        else:
            print("not found")
            return None
    except DatabaseError as e:
        print(f"Error occurred during database operation: {e}")
    finally:
        config.database.close_connection(con, cur)


def up_one_date(table, column, value, field_data):
    con = config.database.get_connection()
    try:
        with con:
            cur = con.cursor()
            sql = "UPDATE {} SET {} = %s WHERE id = %s".format(table, column)
            cur.execute(sql, (value, field_data))
            con.commit()
            print("update OK")
    except DatabaseError as e:
        print(f"Error occurred during database operation: {e}")
    finally:
        config.database.close_connection(con, cur)
