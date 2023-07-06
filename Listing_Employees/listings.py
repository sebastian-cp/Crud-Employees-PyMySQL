import pymysql

class Listings:
    def __init__(self):
        self.connection=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="employees"
        )
        self.cursor=self.connection.cursor()

    def list_manager(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE position='manager'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_HHRR_manager(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE position='HHRR_manager'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_HHRR(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE position='HHRR'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_worker(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE position='worker'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_female_employees(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE sex='female'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise        

    def list_male_employees(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE sex='male'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise        

    def see_list_employees(self):
        sql = "SELECT name, last_name, position, area FROM employees"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def see_employee_information(self, rut):
        sql = "SELECT * FROM employee WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employee found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_RCP(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE area='rcp'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise
    
    def list_CS(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE area='cs'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_LD(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE area='ld'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise
    
    def list_AF(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE area='af'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_IT(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE area='it'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_RCP_D(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE departament='rcp_d'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise
    
    def list_CS_D(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE departament='cs_d'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_LD_D(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE departament='ld_d'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise
    
    def list_AF_D(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE departament='af_d'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise

    def list_IT_D(self):
        sql = "SELECT name, last_name, position, area FROM employees WHERE departament='it_d'"
        try:
            self.cursor.execute(sql)
            empl = self.cursor.fetchall()

            if len(empl) == 0:
                raise Exception("No employees found.")

            for emp in empl:
                print("-----------------------------------")
                print("Name: ", emp[1])
                print("Last Name: ", emp[2])
                print("Position: ", emp[6])
                print("Area: ", emp[7])
                print("Departament", emp[8])
                print("-----------------------------------")
        except Exception as e:
            raise
        
listings=Listings()