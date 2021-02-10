import mysql.connector, os, re

SQLpassword = os.environ.get('Passw0rd')
print(SQLpassword) 
con = mysql.connector.connect(
   host="127.0.0.1",
   user="root",
   password="Passw0rd",
  database="clients"
)

cur = con.cursor()

def welcomePage():
    isValid = False
    while isValid == False:
        username = input('Insert username\n')
        Passwordinput = input('Insert Password\n')
        checkValid = f"""SELECT password FROM `clientinfo` WHERE username='{username}'"""
        cur.execute(checkValid)
        storedPassword = cur.fetchone()[0]
        if  Passwordinput == storedPassword:
            print('Welcome')
            isValid = True
        else:
            print('Login Unsuccsessful')

def register():
    isValid = False
    isINDB = False
    while isValid == False and isINDB == False:
        username = input('Insert Username\n')
        isValid = re.match(r'^[a-zA-Z0-9!$%?@]{6,10}$', username)
        email = input('Insert email\n')
        isValid = re.match(r'^[a-zA-Z0-9!$%?@]{6,10}$', email)
        password = input('Insert password\n')
        isValid = re.match(r'^[a-zA-Z0-9!$%?@]{6,10}$', password)
        if username and email and password:
            print('Successful')
            isValid = True
            isINDB = uniqueID(username)
            if isINDB == False:
                register = f"""INSERT INTO `clientinfo` VALUES ('{username}', '{email}', '{password}')"""
                cur.execute(register)
                con.commit()
                isINDB = True
                print('Registration Successful')
            else:
                print('User already exists! try again')

def uniqueID(username):
    isinDB = True
    searching = f"""SELECT password FROM `clientinfo` WHERE username='{username}' """
    cur.execute(searching)
    isinDB = cur.fetchone()
    if isinDB:
        print('Name already in use!\n')
    else:
        isinDB = False

    return isinDB

def overall():
    isValid = False
    while isValid == False:
        option = int(input('Welcome to The Peoples Bank\n' '1 Please select 1.login or 2.register or 3.exit\n'))
        if option == 1:
            isValid = True
            welcomePage()
        elif option == 2:
            isValid = True
            register()
        elif option == 3:
            print('Session terminated')
            isValid = True


overall()


