import os, json, uuid,sys

with open('hotels.json', 'r') as f:
    data = json.load(f)

def book_room() :
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
