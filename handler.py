import psycopg2
import psycopg2.extras
from config import Config

conf = Config()


class Handler:
    INSERT_SCRIPT = """INSERT INTO expense
     (spender, category, amount, account, description)
     VALUES (%s, %s, %s, %s, %s)"""
    DELETE_SCRIPT = "DELETE FROM expense WHERE id = {}"
    SUM_SCRIPT = "SELECT SUM(amount) FROM expense WHERE account = '{}';"

    def __init__(self):
        self._con = self._connect()

    def _connect(self):
        return psycopg2.connect(
            host=conf.HOSTNAME,
            dbname=conf.DATABASE,
            user=conf.USERNAME,
            password=conf.PASSWORD,
            port=conf.PORT_ID,
        )

    def _close(self):
        self._con.commit()
        self._con.close()

    def add_expense(self, inserted_values):
        with self._con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            if cursor is None:
                print("Nothing added! Please add >cursor< object")
            else:
                if inserted_values is None:
                    print("Nothing added! No values added!")
                else:
                    cursor.execute(self.INSERT_SCRIPT, inserted_values)
                    print("Record successfully added to DB!")
            self._con.commit()

    def select_all(self):
        with self._con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("SELECT * FROM expense")
            return cursor.fetchall()

    def summ_up_account(self, acc_name):
        with self._con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            if cursor is None:
                pass
            else:
                cursor.execute(self.SUM_SCRIPT.format(acc_name), acc_name)
                record = cursor.fetchall()
                print(record)
                if record == [[None]]:
                    return [[float(0.0)]]
                else:
                    return record

    def remove_expense(self, identifier):
        with self._con.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            if cursor is None:
                print("Nothing removed! Please add >cursor< object")
            else:
                if identifier is None:
                    print("Nothing removed! No identfier.")
                else:
                    cursor.execute(self.DELETE_SCRIPT.format(identifier))
                    print("Record successfully removed from DB!")
            self._con.commit()

# DB CREATION BACKUP - SQL CODE

# CREATE TABLE spender (
# 	id SERIAL PRIMARY KEY,
# 	username varchar(30) NOT NULL UNIQUE,
# 	email varchar(64) UNIQUE,
# 	password_hash varchar(128))

# CREATE TABLE expense (
# 	id SERIAL PRIMARY KEY,
# 	spender varchar(30) NOT NULL,
# 	category varchar(64) NOT NULL,
# 	amount decimal(9,2),
# 	account varchar(60),
# 	description varchar(500))
