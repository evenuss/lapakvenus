import pymysql

connection = pymysql.connect (
    host='localhost',
    user='root',
    password='',
    db='db_lapakvenus',
)

print("=====INPUT DATA KATEGORI BARANG=====")
kd_kategori = input ("Kd Kategori : ")
kategori = input ("Kategori : ")

try:
    with connection.cursor () as cursor:
        sql = "INSERT INTO tb_kategori VALUES (%s, %s)"

        try:
            cursor.execute (sql, (kd_kategori, kategori))
            print ("Berhasil")
        except:
            print ("Gagal")

    connection.commit ()
finally:
    connection.close ()