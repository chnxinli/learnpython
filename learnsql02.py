import pymysql

def main():
   
    passwd = input('输入密码： ')
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password=passwd,
                           db='iris',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    
    try :
        with conn.cursor() as cursor:
            sql="select * from iris where sepal_width > 4;"
            cursor.execute(sql)
            for row in cursor.fetchall():
                print(row['sepal_length'])
    finally:
        conn.close()            


if __name__ == "__main__":
    main()