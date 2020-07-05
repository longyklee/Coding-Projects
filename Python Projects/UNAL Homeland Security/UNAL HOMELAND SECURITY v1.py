#UNITED NATIONS OF AARONLAND CUSTOMS (UNAL CUSTOMS)
import sys
import random
import time

print("(C) 2019 UNAL HOMELAND SECURITY")
print("*****ALL INFORMATION IS CONFIDENTIAL*****")
input("Press Enter to START")
passcode = 991467
entered_passcode = eval(input("Please Enter the PIN code: "))
if passcode == entered_passcode:
    print("PASS!")
    time.sleep(.5)
    print("Jobs include:")
    print("1. Arrivals                            2. Departures")
    print("3. Find Criminal                       4. Generate Access Code")
    print("5. Find Citizens                       6. EXIT Program")
    job = eval(input("Select your job: "))
    time.sleep(.5)
    print("")

    if job == 1:
        print("1. ARRIVALS")
        people_type = eval(input("0. Citizens/ 1. Visitors/ 2. Military: "))
        if people_type == 0:
            idnum = eval(input("Please enter identify code (10 digits): "))
            origin = eval(input("Origin (Codes 2-3): "))
            print("Loading System...  Finding Database...")
            time.sleep(2)
            if 1000000000 < idnum < 9999999999 and 10 < origin < 999:
                print("ID Number", idnum, "has NO criminal records and is APPROVED for access!")
                input("Press Enter to EXIT")
                sys.exit(0)
            else:
                print("ID Number and/or Origin Code is NOT VALID!")
                input("Press Enter to EXIT")
                sys.exit(0)
        if people_type == 1:
            country = eval(input("Please enter International Countries Code (ICC) (2-3 digits): "))
            print("Loading...")
            time.sleep(2)
            if 10 < country < 999:
                print("Country Verified")
                idnum = eval(input("Please enter identify code (Codes may vary as ICC): "))
                origin = eval(input("Origin (Codes 2-3): "))
                print("Loading...")
                time.sleep(2)
                if 10000 < idnum < 99999999999999999999 and 10 < origin < 999:
                    print("ID Number, ",idnum, "from country code ",country, "is VALID and is APPROVED for access!")
                else:
                    print("ID Number and/or Origin Code is NOT VALID!")
            else:
                print("Code is NOT VALID")
            input("Press Enter to EXIT")
            sys.exit(0)
        if people_type == 2:
            idnum = eval(input("Please enter identify code (7 digits): "))
            origin = eval(input("Origin (Codes 2-3): "))
            print("Loading System...  Finding Database...")
            time.sleep(2)
            if 1000000 < idnum < 9999999 and 10<origin<999:
                print("ID Number", idnum ,"is CLEARIFIED as a Military partner and is APPROVED for access!")
                input("Press Enter to EXIT")
                sys.exit(0)
            else:
                print("ID Number and/or Origin Code is NOT VALID!")
                input("Press Enter to EXIT")
                sys.exit(0)
        else:
            print("Wrong Code!")
            input("Press Enter to EXIT")
            sys.exit(0)
            
    if job == 2:
        print("1. ARRIVALS")
        people_type = eval(input("0. Citizens/ 1. Visitors/ 2. Military: "))
        if people_type == 0:
            idnum = eval(input("Please enter identify code (10 digits): "))
            print("Loading System...  Finding Database...")
            destination = eval(input("Destination (Codes 2-3): ")) 
            time.sleep(2)
            if 1000000000 < idnum < 9999999999 and 10<destination<999:
                print("ID Number", idnum, "has NO criminal records and is APPROVED for access!")
                input("Press Enter to EXIT")
                sys.exit(0)
            else:
                print("ID Number and/or Destination Code is NOT VALID!")
                input("Press Enter to EXIT")
                sys.exit(0)
        if people_type == 1:
            country = eval(input("Please enter International Countries Code (ICC) (2-3 digits): "))
            print("Loading...")
            time.sleep(2)
            if 10 < country < 999:
                print("Country Verified")
                idnum = eval(input("Please enter identify code (Codes may vary as ICC): "))
                destination = eval(input("Destination (Codes 2-3): ")) 
                print("Loading...")
                time.sleep(2)
                if 10000 < idnum < 99999999999999999999 and 10<destination<999:
                    print("ID Number,",idnum, "from country code ",country, "is VALID and is APPROVED for access!")
                else:
                    print("ID Number and/or Destination Code is NOT VALID!")
            else:
                print("Code is NOT VALID")
            input("Press Enter to EXIT")
            sys.exit(0)
        if people_type == 2:
            idnum = eval(input("Please enter identify code (7 digits): "))
            destination = eval(input("Destination (Codes 2-3): "))
            print("Loading System...  Finding Database...")
            time.sleep(2)
            if 1000000 < idnum < 9999999 and 10<destination<999:
                print("ID Number", idnum ,"is CLEARIFIED as a Military partner and is APPROVED for access!")
                input("Press Enter to EXIT")
                sys.exit(0)
            else:
                print("ID Number and/or Destination Code is NOT VALID!")
                input("Press Enter to EXIT")
                sys.exit(0)
        else:
            print("Wrong Code!")
            input("Press Enter to EXIT")
            sys.exit(0)
            
    if job == 3:
        print("3. FIND CRIMINAL")
        criminalcode = eval(input("Please enter CRIMINAL CODE (5 digits): "))
        print("Loading...")
        time.sleep(2)
        if 10000 < criminalcode < 99999:
            input("This code represents a criminal. Press Enter to EXIT")
        else:
            input("Sorry, CODE not found, press Enter to EXIT")
        sys.exit(0)

    if job == 4:
        print("4. GENERATE ACCESS CODE")
        print("Generating...")
        time.sleep(1)
        print("Access code is ",random.randint(1000, 9999))
        input("Press Enter to EXIT")
        sys.exit(0)

    if job == 5:
        print("5. FIND CITIZENS")
        idnum = eval(input("Please enter identify code (10 digits): "))
        print("Loading...")
        time.sleep(2)
        if 1000000000 < idnum < 9999999999:
            print("This citizen is VALID")
        else:
            print("This citizen is NOT VALID")
        input("Press Enter to EXIT")
        sys.exit(0)

    if job == 6:
        input("Press Enter to EXIT")
        sys.exit(0)
        
else:
    print("Wrong Code, reporting to UNAL Crime SYSTEM...")
    input("Press Enter to EXIT")
    sys.exit(0)

