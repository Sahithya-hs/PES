users = []
x = dict()
spl_chars = ['!','/','.','@','*','&','^','%','$','#','(',')','-','+','=']
num_of_users = 0
while(num_of_users<5):
    print("\n 1.Create\n 2.Existing Users")
    choice=int(input())
    if choice == 1:
        flag = True
        while(flag):
            #creating a user
            fname = str(input("Enter Your First name : "))
            sname = str(input("Enter Your Second name:"))
            twitter_handle = "@"+fname.capitalize()+sname.capitalize()
            #checking if username is already taken
            if(twitter_handle not in users):
                users.append(twitter_handle)
                flag = False
            
            else:
                print("Username already taken")

        else:
            flag = True
            while(flag):
                flag2 = True
                password = input("Please enter a password:")
                for i in password:
                    if(i in spl_chars):
                        flag2 = False
                        break
                if(len(password)>=8 and password[0].isalpha() and flag2):
                    x[twitter_handle] = password
                    flag = False
                else:
                    print("Invalid password. Use atleast 8 characters.")
            else:
                print("Welcome "+twitter_handle)

        num_of_users+=1
    elif choice==2:
        print(users)
    else:
        exit(0)
