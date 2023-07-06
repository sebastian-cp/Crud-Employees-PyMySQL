import pymysql

class Creates:
    def __init__(self):
        self.connection=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="employees"
        )
        self.cursor=self.connection.cursor()

    def create_new_employee(self, name, last_name, rut, sex, address, phone, position, date_entry, area, department):
        sql = "INSERT INTO employee(name, last_name, rut, sex, address, phone, position, date_entry, area, department) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name, last_name, rut, sex, address, phone, position, date_entry, area, department)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise

    def create_new_credentials(self, name, password, rut_employee):
        sql = "INSERT INTO credentials(name, password, rut_employee) VALUES('{}','{}','{}')".format(name, password, rut_employee)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise

    def create_emergency_contact(self, contact_name, contact_relationship, contact_phone, rut_employee):
        sql = "INSERT INTO emergency_contact(contact_name, contact_relationship, contact_phone, rut_employee) VALUES('{}','{}','{}')".format(contact_name, contact_relationship, contact_phone, rut_employee)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise

    def create_family_burden(self, burden_name, burden_last_name, burden_realtionship, burden_phone, rut_employee):
        sql = "INSERT INTO family_burden( burden_name, burden_last_name, burden_realtionship, burden_phone, rut_employee) VALUES('{}','{}','{}','{}')".format( burden_name, burden_last_name, burden_realtionship, burden_phone, rut_employee)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            
        except Exception as e:
            raise

creates=Creates()


