import pymysql

class Updates:
    def __init__(self):
        self.connection=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="employees"
        )
        self.cursor=self.connection.cursor()

    def update_employee_address(self, address, rut):
        sql = "UPDATE employee SET address='{}' WHERE rut='{}'".format(address, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def update_employee_phone(self, phone, rut):
        sql = "UPDATE employee SET phone='{}' WHERE rut='{}'".format(phone, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise


    def update_employee_salary(self, salary, rut):
        sql = "UPDATE employee SET salary='{}' WHERE rut='{}'".format(salary, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def update_employee_position(self, position, rut):
        sql = "UPDATE employee SET position='{}' WHERE rut='{}'".format(position, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def update_employee_area(self, area, rut):
        sql = "UPDATE employee SET area='{}' WHERE rut='{}'".format(area, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise
    
    def update_employee_departament(self, departament, rut):
        sql = "UPDATE employee SET departament='{}' WHERE rut='{}'".format(departament, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def update_phone_family_burden(self, burden_phone, rut):
        sql = "UPDATE family_burden SET burden_phone='{}' WHERE rut_employee='{}'".format(burden_phone, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise


    def update_emergency_contact_name(self, contact_name, rut):
        sql = "UPDATE emergency_contact SET contact_name='{}' WHERE rut_employee='{}'".format(contact_name, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def update_emergency_contact_relationship(self, contact_relationship, rut):
        sql = "UPDATE emergency_contact SET contact_relationship='{}' WHERE rut_employee='{}'".format(contact_relationship, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise
        
    def update_emergency_contact_phone(self, contact_phone, rut):
        sql = "UPDATE emergency_contact SET contact_phone='{}' WHERE rut_employee='{}'".format(contact_phone, rut)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

updates=Updates()
