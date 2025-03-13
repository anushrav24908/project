import pickle
def Write():
    f=open('StudentDetails.dat','wb')
    while True:
        r=int(input("Roll Number :"))
        n=input("Enter Name :")
        Data=[r,n]
        pickle.dump(Data,f)
        ch=input('More ?? (Y/N)')
        if ch in 'Nn':
            break
    f.close()

def Search():
    found=0
    rollno=int(input("Enter Roll No Whose Name u Want to Display :"))
    f=open('StudentDetails.dat','rb')
    try:
        while True:
            rec=pickle.load(f)
            if rec[0]==rollno:
                print(rec[1])
                found=1 # only when the roll no is found
                break
    except EOFError:
        f.close()
    if found==0:
        print("Sorry !!! No Record Found ....")
Write()
Search()       
