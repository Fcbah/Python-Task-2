import random
import string

alphabets = string.ascii_letters

def getRandomletters(length):
    output = ""
    for x in range(length):
        output += random.choice(alphabets)
    return output

# Must be 9 digit long ...
def create_default_password(firstName,lastName):
    password = ""

    # extract first two letters from first name
    # and  last two letters from lastname
    password += firstName[:2]
    password += lastName[-2:]

    # generate 4 random letters
    password += getRandomletters(4)

    return password

def get_user_preffered_password():
    tmp_pass = input("Enter Your Preffered Password: ")
    while len(tmp_pass) < 7:
        tmp_pass = input("\nINVALID PASSWORD\nPlease Enter another password with at least 7 characters: ")
    return tmp_pass

def print_user_details(user_entry):
    for key,val in user_entry.items():
        print("%s: \t\t%s"%(key,val))

def print_all_entries(entries):
    print('.............................ALL RECORDS.............................\n')
    for entry in entries:
        print('***************************************************')
        print_user_details(entry)


if __name__ == "__main__":
    q = ["First Name\t", "Last Name\t", "Email\t\t"] #I added this whitespace to make the final presentation of user details nice 
    passs = "Password\t"
    user_entry = {}
    Entries=[]

    print("---------------------------------------------------------------------------")
    print("Employe details collector for HNG TECH - By Fcbah (Akinleye Hephzibah)")

    while True:
        user_entry = user_entry.copy() #This is important to ensure that a new user entry does not wipe out previous ones
        
        print('************************************************************************')
        for entry in q:
            user_entry[entry] = input("Please enter your '%s' : "%entry.lower().rstrip())
        
        user_entry[passs] = create_default_password(user_entry[q[0]],user_entry[q[1]])

        print("*************************************************************")
        print("Your Default Password is: %s"%user_entry[passs])
        if input("\nPress 'ENTER' to retain your default password OR ANY OTHER KEY to change it\n") != '' :
            user_entry[passs] = get_user_preffered_password()

        print("****************************************************************************")
        print("%s, your details are now given below:\n"%user_entry[q[0]])
        print_user_details(user_entry)       

        Entries.append(user_entry)

        if input("\nPress ANY OTHER KEY to enter another employee's details OR Press 'Q' to QUIT \n").lower() == 'q':
            print_all_entries(Entries)            
            break
        
