import pickle

login = 0

password = 0

fail = True

login_or = 0

# dictionairy list to map one value to another, {} brackets for dictionairy
# stored like this: username : password
# like {'username': 'password, ...}

users = {} 


# chooses if proceeding with login or registration depending on input

def login_question():
    global login_or
    login_or = input("Do you want login or reg? enter a or b : ")
    if login_or == "a":
         enter_login()
         login_function()
    elif login_or == "b":
         enter_reg()
    else:
        print(f'invalid input please type a or b')
        login_question()


#enter login data function

def enter_login():
    global login
    global password
    login = input("Enter username: ")
    password = input("Enter password: ")
    

#check login input with dictionairy data

def login_function():
    global login
    global password
    global fail
    global users


    if login in users and users[login] == password:
        print(f'Login successful!')
        fail == False

    else:
        print(f'Login invalid')
        fail == True
        login = input("Enter username: ")
        password = input("Enter password: ")
        login_function()

#registration function, append/add users

def enter_reg():
    global users
    reg_username = input("USER: ")
    reg_pw = input("pw: ")
    users[reg_username] = reg_pw

    #adds new username and password in .pkl file (and creates it if not exist)

    with open('saved_dictionary.pkl', 'wb') as f:
        pickle.dump(users, f)
        print(users)


  #load .pkl file dictionairy with usernames and passwords

try: 
    with open('saved_dictionary.pkl', 'rb') as f:
         users = pickle.load(f)

except: #if not

    print(f'No file with users found, please proceed now with registering an account: ')
    enter_reg()

print(users)

#ask if login or registration

#login_question()

import curses
from curses import wrapper


mywindow = curses.initscr()

curses.curs_set(0)
curses.start_color()
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

def updateMatrix(m):
    m[1][1] = m[1][1] * 2
    return m

def getMarixString(m,selected_row_index,selected_col_index, enter_Pressed = False):
    x = ''
    i = 0
    for row in m:
        j = 0
        for el in row:
            if enter_Pressed == True:
                enter_Pressed = False
                mywindow.addstr(i, j, str(8))
            elif i == selected_row_index and j == selected_col_index:
                mywindow.attron(curses.color_pair(1))
                mywindow.addstr(i, j, str(el))
                mywindow.attroff(curses.color_pair(1))
            else:
                mywindow.addstr(i, j, str(el))
            j += 2
        i += 1
        #x += ' '.join(str(item) for item in row)
        #x += "\n"
    return x

#z = 10
#while z > 1:
    #matrix = updateMatrix(matrix)
#curses.echo()  # Enable echoing of characters
curses.echo()
curses.cbreak()


# Get a 15-character string, with the cursor on the top line
s = mywindow.getstr(0, 0, 15)
int_num = int(s)
mat = []
mywindow.keypad(True)
row_header = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J']
row_header = row_header[:int_num]
col_header = [i for i in range(int_num)]
for i in range(int_num):
    row = [row_header[i]+') ']
    for j in range(int_num):
        val = '~'
        row.append(val)
    mat.append(row)
#col_header = col_header.insert(0, ' ')
mat.append(['   ']+col_header)
#mywindow.addstr(0, 0, getMarixString(mat))
getMarixString(mat,0,2, False)
mywindow.refresh()
current_row_idx = 0
current_col_index = 2
#z -= 1
enterPressed = False
while 1:
    #mywindow.clear()
    key = mywindow.getch()
    mywindow.clear()
    if key == curses.KEY_RIGHT and current_col_index < 2*(len(mat)) -2:
        current_col_index += 2
    elif key == curses.KEY_LEFT and current_col_index > 3:
        current_col_index -= 2
    elif key == curses.KEY_UP and current_row_idx > 0:
        current_row_idx -= 1
        #mywindow.addstr(0,0,"UP")
    elif key == curses.KEY_DOWN and current_row_idx < int_num - 1:
        current_row_idx += 1
        #mywindow.addstr(0, 0, "Down")
    elif key == curses.KEY_ENTER or key in [10.13]:
        #mywindow.addstr(0, 0, "Enter")
        enterPressed = True
    #print(current_row_idx)
    getMarixString(mat, current_row_idx,current_col_index, enter_Pressed = enterPressed)
    mywindow.refresh()
5#time.sleep(10)10
mywindow.getch()

curses.endwin()
quit()
