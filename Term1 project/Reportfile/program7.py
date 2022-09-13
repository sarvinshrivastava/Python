print("Program to create a csv file by entering user id and password read and search the password for given user")
answer = input("Do you have an account?(yes or no) ")
if answer == 'yes' :
   login = False
   csvfile = open("Username password.csv","r")
   reader = csv.reader('Username password.csv')
   username = input("Username: ")
   password = input("Password: ")
   for row in reader:
        if row[0]== username and row[1] == password:
           login = True
        else:
           login = False
   if login == False:
      print("Incorrect username or password")
      exit()
   else:
      print("You are now logged in!")
else:
   print('Only Valid Usernames can login!')
   exit()
