import pymysql


class Host(object):
    def __init__(self, id, hostname, ip, created_at, updated_at):
        self.id = id
        self.hostname = hostname
        self.ip = ip
        self.created_at = created_at
        self.updated_at = updated_at


def get_db():
    conn = pymysql.connect(
        host="",
        port=3306,
        database="host",
        charset="utf8",
        user="root",
        passwd="root",
        cursorclass=pymysql.cursors.DictCursor  # 以字典的形式返回数据
    )
    return conn


def query_host(db):
    res = []
    mycursor = db.cursor()  # 和前面一样，下面为了简洁统统省略
    mycursor.execute(
        "SELECT id,hostname,ip,created_at, updated_at FROM host limit 1")  # 执行sql语句，结果赋给mycursor
    myresult = mycursor.fetchall()  # 用了 fetchall() 方法，该方法从最后执行的语句中获取所有行，结果赋给myresult。
    for index, row in enumerate(myresult):
        host = Host(**row) 
        print(host.id, host.hostname)
        res.append(host)
    return res


def insert_host(db):
    pass


def delete_host(db):
    pass


def update_host(db):
    pass


if __name__ == '__main__':
    db = get_db()
    res = query_host(db)
    for r in res:
        print(r)
    db.close()
