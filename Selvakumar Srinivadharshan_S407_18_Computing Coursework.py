#Import stuff
import pickle
import random

#Encrypt Function
#Normal Text ---> Encrypted Text
def Cipher(norTxt,val):
     decTxt = ""
     #Find shift Value
     val = int(val)
     for i in norTxt:
          #Find ASCII Number and add shift
          if ord(i) >= 65 and ord(i) <= 90:
               newnum = int(ord(i)+val)
               if newnum >90:
                    newnum = 64+(newnum - 90)
               i = chr(newnum)
               decTxt += i
          elif ord(i) >= 97 and ord(i) <= 122:
               newnum = int(ord(i)+val)
               if newnum >122:
                    newnum = 97+(newnum - 122)
               i = chr(newnum)
               decTxt += i
          else:
               #If character is not a letter, just add it the same
               decTxt += i
     return(decTxt)

#Decrypt Function
#Encrypted Text ---> Decrypted Text
def DeCipher(decTxt,val):
     norTxt = ""
     #Find shift Value
     val = int(val)
     for i in decTxt:
           #Find ASCII Number and minus shift
          if ord(i) >= 65 and ord(i) <= 90:
               newnum = int(ord(i)-val)
               if newnum < 65:
                    newnum = 91 - (65 - newnum)
               i = chr(newnum)
          elif ord(i) >= 97 and ord(i) <= 122:
               newnum = int(ord(i)-val)
               if newnum <97:
                    newnum = 122-(97 - newnum)
               i = chr(newnum)
            #If character is not a letter, just add it the same
          norTxt += i
     return(norTxt)


try: 
    #Check if user has account by checking if textfile exist
    Account = open("Account34Det.txt", "r")
except:
    #Create account if text file is not found
    print("Hi! You must be a first time user. Please create an account")
    #get inputs for password and username
    CrAcc = open("Account34Det.txt", "w")
    UName = input("Type your username : ")
    #write password and username to textfile
    CrAcc.write(UName)
    CrAcc.write("\n")
    PWord = input("Type your password : ")
    print("")
    CrAcc.write(PWord)
    CrAcc.close()
else:
    #Open file text
    Account = open("Account34Det.txt", "r")
    #Get info from file text
    Username = Account.readline()
    Password = Account.readline()
    Account.close()

    #Login
    checked = False
    while checked != True:
        askPW = str(input("Login - Type your password to log in : "))
        if askPW != Password:
            print("Try again")
        elif askPW == Password:
            checked = True
            print("")
            print("Access granted")
            print("Greeetings",Username)
            print("What would you like to do today?")
            print("")

            doneFull = False #Loop so that user can repeat again and again
            while doneFull != True:
                inp = str(input("Type 'A' for password generator, 'B' for password strength checker and 'C' for Password Manager : "))

                #PasswordGenerator
                if inp == "A":
                    X = False
                    while X != True:
                        #Get memorable text
                        prefTxt = input("Memorable text to be embedded in your password(At least 16 characters long) : ") 
                        #Make sure length is enough(More than 16)
                        if len(prefTxt) >= 16:X = True
                        else:print("Text should be at least 16 characters long")
                    
                    #Replace some letters in text with numbers and symbols
                    prefTxt = prefTxt.replace("e","3")
                    prefTxt = prefTxt.replace("E","3")
                    prefTxt = prefTxt.replace("s","5")
                    prefTxt = prefTxt.replace("S","5")
                    prefTxt = prefTxt.replace("O","0")
                    prefTxt = prefTxt.replace("o","0")
                    prefTxt = prefTxt.replace("i","¡")
                    prefTxt = prefTxt.replace("I","¡")

                    #choose 4 random letters from text and change their capitalisation
                    for i in range(4):
                        letter = random.choice(prefTxt)
                        if letter.isalpha():
                            if letter.isupper():
                                prefTxt = prefTxt.replace(letter,letter.lower())
                            if letter.islower():
                                prefTxt = prefTxt.replace(letter,letter.upper())

                    #Output changed password
                    print("You can use this as your new Password :",prefTxt)

                    #Checkif use wants to end
                    end = input("Type X to end, press enter if you still wish to use this program : ")
                    if end == "X":
                        break

                #PasswordStrengthChecker
                if inp == "B":
                    strengthLevel = ["Weak","Moderate","Pretty Strong","Very Strong"] #The various strength levels
                    password = input("Type your password: ")  
                    strength = 0
                    caps = False
                    symb = False
                    num = False
                    low = 0
                    upp = 0

                    if len(password) > 16: #Check length
                        strength += 1
                    else:
                        print("- Try to make password at least 16 letters long") # Give feedback on how to improve
                    for i in password:
                        if i.isalnum() != True:symb = True #Check for instances of symbols
                        if i.islower() == True:low+=1 #Check for instances of lowercase letters
                        if i.isupper() == True:upp+=1 #Check for instances of uppercase letters
                        if i.isnumeric() == True: num = True #Check for instances of numbers

                    if num == True: #Check for numbers
                        strength+=1
                    else:
                        print("Try to add numbers") # Give feedback on how to improve

                    if symb == True: #Check for symbols
                        strength += 1
                    else:
                        print("- Try to add symbols") # Give feedback on how to improve
                    
                    if low>0 and upp>0: #Check for lowercase and uppercase
                        strength += 1
                    else:
                        print("- Try to use both lowercase and uppercase letters") # Give feedback on how to improve
                
                    print("Your password strength level is",strengthLevel[strength]) #Output the strength level
                    
                    #Check if user wishes to end
                    end = input("Type X to end, press enter if you still wish to use this program : ") 
                    if end == "X":
                        break
                    else:
                        doneFull = False

                #Password Manager
                if inp == "C":
                #Print Title
                    print("Password and Username Manager")
                    print()
                    #Get input
                    act = input("Do you want to add data or read data [A/R] : ")
                    if act == "A":
                        #getting data from input
                        s = ""
                        u = ""
                        p = ""
                        #Repeat until not input is not empty
                        while s == "": s = input("Site : ") 
                        while u == "": u = input("Username : ")
                        while p == "": p = input("Password : ")
                        #encrypt text
                        s =  Cipher(s,7)
                        u =  Cipher(u,7)
                        p =  Cipher(p,7)
                        try:
                            #Check if file already exists or if this is the first input
                            with open('PickleData.pkl', 'rb') as f: data = pickle.load(f)
                        except:
                            #Create new file
                            data = []
                            d = {"Site":s,"Uname":u,"Password":p} #Add in format of dictionary
                            data.append(d) # Add data 
                            with open('PickleData.pkl', 'wb') as f: pickle.dump(data, f)
                        else:
                            #Get old data
                            with open('PickleData.pkl', 'rb') as f:data = pickle.load(f) 
                            d = {"Site":s,"Uname":u,"Password":p}#Add in format of dictionary
                            data.append(d) #Add to old data
                            with open('PickleData.pkl', 'wb') as f: pickle.dump(data, f)
                    
                    elif act == "R":
                        try:
                            #Check if user has file first
                            with open('PickleData.pkl', 'rb') as f: data = pickle.load(f)
                        except :
                            #Add Data if no file is present
                            print("You have no data. Write some first")
                            s = ""
                            u = ""
                            p = ""
                            #Repeat until not input is not empty
                            while s == "": s = input("Site : ")
                            while u == "": u = input("Username : ")
                            while p == "": p = input("Password : ")
                            data = []
                            #encrypt text
                            s =  Cipher(s,7)
                            u =  Cipher(u,7)
                            p =  Cipher(p,7)
                            d = {"Site":s,"Uname":u,"Password":p} #Add in format of dictionary
                            data.append(d) #Add Data
                            with open('PickleData.pkl', 'wb') as f:
                                pickle.dump(data, f)
                        else:
                            #Give choices avaliable
                            print("Avaliable sites with data")
                            print("="*60)
                            print("|",end="")
                            for i in data:
                                site = i["Site"]
                                site = DeCipher(site,7)
                                print(site,end="|")
                            print()

                            #Get which site's data they need
                            site = input("site : ")
                            found = False
                            #Check if input exists
                            for d in data:
                                dSite = DeCipher(d["Site"],7)
                                if dSite == site:
                                        found = True
                                        # Output data
                                        print("Username : {}".format(DeCipher(d["Uname"],7)))
                                        print("Password : {}".format(DeCipher(d["Password"],7)))
                            if found == False: # If input given doesn't exist
                                print("No suitable data found for this site")
                    else: # If input given is wrong
                        print("Invalid Input")
                        
                # Check if user wants to end program
                end = input("Type X to end, press enter if you still wish to use this program : ")
                if end == "X":
                    break
                                
