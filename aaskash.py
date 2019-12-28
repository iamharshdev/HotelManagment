import os, json, uuid,sys
from book import book_room

with open('hotels.json', 'r') as f:
    data = json.load(f)

def bookroom() :
    print("Room Details:-")
    print("*****************")
    print("AC Rooms = 1 - 10")
    print("Normal Rooms = 11 - 30")
    room_no=input("Enter room no. which customer wants to book: ")
    with open('hotels.json', 'r') as f:
        data = json.load(f)
    if room_no in data :
        print('Sorry Rom is not vacant')
    else:
        cnm=input("Enter Customer's Name: ")
        mob=input("Enter Phone Number: ")
        aadhr=input("Enter Aadhar Number: ")
        add=input("Enter Address: ")
        room_no=int(room_no)
        if room_no>=1 and room_no<=10:
            roomtype="AC"
        elif room_no>=11 and room_no<=30:
            roomtype="NON-AC"
        var =  {
                "Customer_Name":cnm,
                "Phone_Number":mob,
                "Addhar_Card_No.":aadhr,
                "Customer_Address":add,
                "Room_type":roomtype
                }

        with open('hotels.json', 'r') as f:
            data = json.load(f)
            data[room_no] = var
    # create randomly named temporary file to avoid
    # interference with other thread/asynchronous request
        tempfile = os.path.join(os.path.dirname('hotels.json'), str(uuid.uuid4()))
        with open(tempfile, 'w') as f:
            json.dump(data, f, indent=4)
    # rename temporary file replacing old file
        os.rename(tempfile, 'hotels.json')
        print("CONGRATUALATIONS!!!!")
        print("ROOM IS BOOKED")

def displayroom() :
    room_no=input("Enter room no. you want : ")
    with open('hotels.json', 'r') as f:
        data = json.load(f)
    if room_no in data :
        print(data[room_no])
    else:
        print("The Room is not booked: ")
        print("Wanna book it again")
        opt=input("Yes if you wanna book or No if you don't wanna book: ")
        optv=opt.upper()
        if optv=='YES':
            book_room()
        elif optv=='NO':
            sys.exit()

def delete_room():
    room_no=input("Enter the room no. of the customer to be deleted: ")
    with open('hotels.json', 'r') as f:
        data = json.load(f)
    if room_no in data:
        del data[room_no]
        tempfile = os.path.join(os.path.dirname('hotels.json'), str(uuid.uuid4()))
        with open(tempfile, 'w') as f:
            json.dump(data, f, indent=4)
                # rename temporary file replacing old file
        os.rename(tempfile, 'hotels.json')
    else:
        print("The Room is not booked: ")
        print("Wanna book it again")
        opt=input("Yes if you wanna book or No if you don't wanna book: ")
        optv=opt.upper()
        if optv=='YES':
            book_room()
        elif optv=='NO':
            sys.exit()

def edit_room():
    room_no=input("Enter the room no. of the customer to be edited: ")
    with open('hotels.json', 'r') as f:
        data = json.load(f)
    if room_no in data:
        cnm=input("Enter Customer's Name: ")
        mob=input("Enter Phone Number: ")
        aadhr=input("Enter Aadhar Number: ")
        add=input("Enter Address: ")
        data[room_no]['Customer_Name'] = cnm
        data[room_no]['Phone_Number'] = mob
        data[room_no]['Addhar_Card_No'] = aadhr
        data[room_no]['Customer_Address'] = add
        tempfile = os.path.join(os.path.dirname('hotels.json'), str(uuid.uuid4()))
        with open(tempfile, 'w') as f:
            json.dump(data, f, indent=4)
                # rename temporary file replacing old file
        os.rename(tempfile, 'hotels.json')

    else:
        print("The Room is not booked: ")
        print("Wanna book it again")
        opt=input("Yes if you wanna book or No if you don't wanna book: ")
        optv=opt.upper()
        if optv=='YES':
            book_room()
        elif optv=='NO':
            sys.exit()

print("*************")
print("MAIN MENU")
print("*************")
print("1. BOOK ROOM ")
print("2. DISPLAY ROOM ")
print("3. EDIT ROOM ")
print("4. DELETE ROOM ")
print("5. EXIT")
choice=input("Please Enter Your Choice :  ")
if choice=='1':
    bookroom()
elif choice=='2':
    displayroom()
elif choice=='3':
    edit_room()
elif choice=='4':
    delete_room()
else:
    sys.exit()
