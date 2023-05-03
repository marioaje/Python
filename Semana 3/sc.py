import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'sql863.main-hosting.eu',
            user = 'u484426513_apireact',
            password = 'i:![VW:3S#',
            db = 'u484426513_apireact'
        )
        self.cursor = self.connection.cursor()
        print('Estoy conectado a una base de datos')

    def select_curso(self, id):
        print('id', id);
        sql = 'SELECT * FROM curso where id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            curso = self.cursor.fetchone()
            print ("nombre:", curso[1])
        except Exception as e:  
            raise  

    def select_all_curso(self):
        sql = 'SELECT * FROM curso'

        try:
            self.cursor.execute(sql)

            curso = self.cursor.fetchall()

            for item in curso:
                print ("id:", item[0])
                print ("Nombre:", item[1])
                print ("Descripcion:", item[2])
                print ("Tiem[p]:", item[3])
                print("_______\n")
                
            

        except Exception as e:  
            raise  
    
    def update_curso(self, id, nombre):
        sql = "UPDATE curso SET nombre='{}' WHERE id = '{}'".format(nombre, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()#es necesario

        except Exception as e:  
            print(e)
            raise  

    def close(self):
        self.connection.close()


database = DataBase()
database.select_curso(14)
database.update_curso(14,'Mario')
database.select_curso(14)
database.close()
#database.select_all_curso()
        # $host = 'sql863.main-hosting.eu';
        # $db_name = 'u484426513_apireact';
        # $username = 'u484426513_apireact';
        # $password = 'i:![VW:3S#';