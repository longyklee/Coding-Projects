#UNITED NATIONS OF AARONLAND CUSTOMS (UNAL CUSTOMS)
import sys
import random
import time
import subprocess

print("(C) 2019 UNAL HOMELAND SECURITY")
print("*****ALL INFORMATION IS CONFIDENTIAL*****")
def program():
    passcode = 991467
    entered_passcode = passcode
    if passcode == entered_passcode:
        print("PASS!")
        while True:
            time.sleep(.5)
            print()
            print("Jobs include:")
            print("1. Arrivals                            2. Departures")
            print("3. Find Criminal                       4. Generate Access Code")
            print("5. Find Citizens                       6. EXIT/ LOCK Program/ EMERGENCY")
            job = input("Select your job: ")
            time.sleep(.5)
            print("")

            if job == 1:
                print("1. ARRIVALS")
                people_type = input("0. Citizens/ 1. Visitors/ 2. Military: ")
                if people_type == 0:
                    idnum = input("Please enter identify code (10 digits): ")
                    name = input("Name: ")
                    origin = input("Origin (Codes 2-3): ")
                    print("Loading System...  Finding Database...")
                    time.sleep(2)
                    if 1000000000 < idnum < 9999999999 and 10 <= origin < 999:
                        print(name, "and ID Number", idnum, "has NO criminal records and is APPROVED for access!")
                        
                        
                    else:
                        print("ID Number and/or Origin Code is NOT VALID!")
                        
                        
                if people_type == 1:
                    country = input("Please enter International Countries Code (ICC) (2-3 digits): ")
                    print("Loading...")
                    time.sleep(2)
                    if 10 < country < 999:
                        print("Country Verified")
                        idnum = input("Please enter identify code (Codes may vary as ICC): ")
                        name = input("Name: ")
                        origin = input("Origin (Codes 2-3): ")
                        print("Loading...")
                        time.sleep(2)
                        if 10000 < idnum < 99999999999999999999 and 10 <= origin < 999:
                            print(name, "and ID Number, ",idnum, "from country code ",country, "is VALID and is APPROVED for access!")
                        else:
                            print("ID Number and/or Origin Code is NOT VALID!")
                    else:
                        print("Code is NOT VALID")
                    
                    
                if people_type == 2:
                    idnum = input("Please enter identify code (7 digits): ")
                    name = input("Name: ")
                    origin = input("Origin (Codes 2-3): ")
                    print("Loading System...  Finding Database...")
                    time.sleep(2)
                    if 1000000 < idnum < 9999999 and 10<origin<999:
                        print(name," and ID Number", idnum ,"is CLEARIFIED as a Military partner and is APPROVED for access!")
                        
                        
                    else:
                        print("ID Number and/or Origin Code is NOT VALID!")

            if job == 2:
                print("2. DEPARTURES")
                people_type = input("0. Citizens/ 1. Visitors/ 2. Military: ")
                if people_type == 0:
                    idnum = input("Please enter identify code (10 digits): ")
                    name = input("Name: ")
                    destination = input("Destination (Codes 2-3): ")
                    print("Loading System...  Finding Database...")
                    time.sleep(2)
                    if 1000000000 < idnum < 9999999999 and 10<=destination<999:
                        print(name, "and ID Number", idnum, "has NO criminal records and is APPROVED for access!")
                        
                        
                    else:
                        print("ID Number and/or Destination Code is NOT VALID!")
                        
                        
                if people_type == 1:
                    country = input("Please enter International Countries Code (ICC) (2-3 digits): ")
                    print("Loading...")
                    time.sleep(2)
                    if 10 < country < 999:
                        print("Country Verified")
                        idnum = input("Please enter identify code (Codes may vary as ICC): ")
                        name = input("Name: ")
                        destination = input("Destination (Codes 2-3): ") 
                        print("Loading...")
                        time.sleep(2)
                        if 10000 < idnum < 99999999999999999999 and 10<=destination<999:
                            print(name, "and ID Number,",idnum, "from country code ",country, "is VALID and is APPROVED for access!")
                        else:
                            print("ID Number and/or Destination Code is NOT VALID!")
                    else:
                        print("Code is NOT VALID")
                    
                    
                if people_type == 2:
                    idnum = input("Please enter identify code (7 digits): ")
                    name = input("Name: ")
                    destination = input("Destination (Codes 2-3): ")
                    print("Loading System...  Finding Database...")
                    time.sleep(2)
                    if 1000000 < idnum < 9999999 and 10<=destination<999:
                        print(name," and ID Number", idnum ,"is CLEARIFIED as a Military partner and is APPROVED for access!")
                        
                        
                    else:
                        print("ID Number and/or Destination Code is NOT VALID!")

            if job == 3:
                print("3. FIND CRIMINAL")
                criminalcode = input("Please enter CRIMINAL CODE (5 digits): ")
                print("Loading...")
                time.sleep(2)
                if 10000 < criminalcode < 99999:
                    input("This code represents a criminal.")
                else:
                    input("Sorry, CODE not found")
                

            if job == 4:
                print("4. GENERATE ACCESS CODE")
                print("Generating...")
                time.sleep(1)
                print("Access code is ",random.randint(1000, 9999)
                
                

            if job == 5:
                print("5. FIND CITIZENS")
                idnum = input("Please enter identify code (10 digits): ")
                print("Loading...")
                time.sleep(2)
                if 1000000000 < idnum < 9999999999:
                    print("This citizen is VALID")
                else:
                    print("This citizen is NOT VALID")
                
                

            if job == 6:
                print("1. Exit                                2. Lock")
                print("3. EMERGENCY")
                eorl = input("Select Job: ")
                if eorl == 1:
                    input("Press Enter to Exit")
                    sys.exit(0)
                if eorl == 2:
                    print("Locking Program... Good Bye!")
                    time.sleep(.75)
                    program()
                if eorl ==3:
                    time.sleep(.5)
                    print("\nSYSTEMS ARMED!!!")
                    time.sleep(.5)
                    print("DISALLOWED ALL CUSTOM GATES!!!")
                    time.sleep(.5)
                    contactnumber = input("ENTER NUMBER TO CONTACT: ")
                    if int(contactnumber)==110 or int(contactnumber)==119 or int(contactnumber)==911:
                        print("CONTACTING POLICE, EXITTING SYSTEM")
                        sys.exit(0)
                    else:
                        exitqq = input("Calling "+contactnumber+"... \nDO YOU WANT TO EXIT SYSTEM? (T/F): ")
                        if exitqq.upper() == 'T' or exitqq == "1":
                            sys.exit(0)
                        if exitqq.upper() == 'F' or exitqq == "0":
                            input("SYSTEMS CONTINUING..\n\n")
            
    else:
        print("Wrong Code, reporting to UNAL Crime SYSTEM...")
        print("1. Exit                                2. Lock")
        eorl = input("Select Job: ")
        if eorl == 1:
            input("Press Enter to Exit")
            sys.exit(0)
        if eorl == 2:
            print("Locking Program... Good Bye!")
            time.sleep(.75)
            program()
        
program()
