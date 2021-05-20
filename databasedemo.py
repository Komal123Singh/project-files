import sqlite3
class Database:

    def __init__(self,name = "db.sqlite3"):
        self.db = sqlite3.connect(name)
        self.create_table()

    def run(self,query):
        try:
            result = self.db.execute(query)
            self.db.commit()
            return result
        except Exception as e:
            print('error---->')
            print(e)
            print('error---->')

    def create_table(self):
        query = """
            create table report(
                id integer primary key autoincrement,
                name text,
                eng integer,
                maths integer,
                science integer,
                hindi integer,
                elective integer
            )
        """
        return self.run(query)

    def add(self,name,eng=0,maths=0,science=0,hindi=0,elective=0):
        query = f"""
            insert into report values(
                null,
                '{name}',
                {eng},
                {maths},
                {science},
                {hindi},
                {elective}
            )
        """
        return self.run(query)

    def view(self):
        query = "select * from report"
        result = self.run(query)
        if result:
            return result.fetchall()
        else:
            return []