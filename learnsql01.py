import pymysql

def main():
    myname=str(input('输入用户： '))
    mypasswd = str(input('输入密码：'))
    # dl =str(input('删除的染色体： '))
    
    conn = pymysql.connect(host='localhost',port=3306,
                        user=myname,password = mypasswd,
                        db ='snps',charset ='utf8',
                        cursorclass=pymysql.cursors.DictCursor)
  
        

                           
    try:
        with conn.cursor() as cursor:
            # result1=cursor.execute('insert into tb_tysnpcompare values("A03",434,"C","G")')
            cursor.execute('select chrom, pos, ttype, ytype from tb_tysnpcompare')
            # for row in cursor.fetchall():
            #     print(f'染色体编号：{row[0]}')
            #     print(f'所在位置：{row[1]}')
            #     print(f'T586碱基类型： {row[2]}')
            #     print(f'渝棉1号碱基类型： {row[3]}')
            #     print('_' *20 )
            # print(cursor.fetchall())
            for row in cursor.fetchall():
                print(row['chrom'])
            # result1 = cursor.execute('delete from tb_tysnpcompare where chrom=%s',(dl,)) #(dl,)元组的意思
            # if result1 ==1 :
            #     print('sucess')
            # conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    main()