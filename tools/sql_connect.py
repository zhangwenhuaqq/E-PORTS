import pymysql
from tools.get_yaml import *

def Mysql_data(sql,data_base):
    db = pymysql.connect(host='139.224.48.247',user='uat_wow_mysql',password='yhUhl#eA2',database=data_base)

    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

    cursor.execute(sql)

    res = cursor.fetchall()

    return res

if __name__=='__main__':

    data1 = get_read(get_file_path('config', 'login.yaml'))
    print(data1)
    print(data1[0]['resp']['sql_data']['SQL'])
    print(data1[0]['resp']['sql_data']['data_base'])
    db1 = Mysql_data(data1[0]['resp']['sql_data']['SQL'],data1[0]['resp']['sql_data']['data_base'])
    print(db1[0]['id'])
