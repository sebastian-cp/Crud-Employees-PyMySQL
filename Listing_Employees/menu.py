import pymysql

class Menu:
    def __init__(self):
        self.connection=pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="employees"
        )
        self.cursor=self.connection.cursor()

    def filter_worker():
        print("1. Sex")
        print("2. Name")
        print("3. Exit")

    def filter():
        print("1. Sex")
        print("2. Position")
        print("3. Area")
        print("4. Departament")
        print("5. Exit")

    def sex():
        print("1. Female")
        print("2. Male")
        print("3. Exit")

    def position():
        print("1. Manager")
        print("2. HH.RR manager")
        print("3. HH.RR")
        print("4. Worker")
        print("5. Exit")

    def area():
        print("1. Reception and classification of packages")
        print("2. Customer Support")
        print("3. Logistics and distribution")
        print("4. Administrative and financial")
        print("5. information technology")
        print("6. Exit")

    def departament():
        print("1. Operations department")
        print("2. Customer service department")
        print("3. Logistics and distribution department")
        print("4. Administrative and financial department")
        print("5. information technology department")
        print("6. Exit")


    def personal_data():
        print("1. Address")
        print("2. Phone")
        print("3. Exit") 

    def family_burden():
        print("1. Phone")
        print("2. Exit")

    def emergency_contact():
        print("1. Name")
        print("2. Relationship")
        print("3. Phone")
        print("4. Exit")

    def modify_employee():
        print("1. Change salary")
        print("2. Change position")
        print("3. Change area")
        print("4. Change departament")
        print("5. Exit")

    def show_worker_menu():
        print("Welcome")
        print("1. List coworkers")
        print("2. Modify my personal data")
        print("3. Exit")

    def show_manager_menu():
        print("Welcome")
        print("1. List employees")
        print("2. manage employees")
        print("3. Modify my personal data")
        print("4. Exit")

    def show_HHRR_menu_():
        print("Welcome")
        print("1. Enter new employee")
        print("2. manage employees")
        print("3. Modify my personal data")
        print("4. Exit")

    def show_HHRR_manager_menu():
        print("Welcome")
        print("1. List employees")
        print("2. Modify my personal data")
        print("3. Exit")

    def check_rut_exists(self, rut):
        sql = "SELECT EXISTS(SELECT 1 FROM employee WHERE rut = '{}');".format(rut)
        try:
            self.cursor.execute(sql)
            Num = self.cursor.fetchone()

        except Exception as e:   
            raise
        return Num

    def confirm_pswrd(self, rut):
        sql = "SELECT password FROM credentials WHERE rut_employee='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            password = result[0] if result else None
        except Exception as e:
            raise

        return password

    def set_position(self,rut):
        sql = "SELECT position FROM employee WHERE rut='{}'".format(rut)
        try:
            self.cursor.execute(sql)
            self.cursor.fetchone()

        except Exception as e:
            raise


menu=Menu()