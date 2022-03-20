from collections import OrderedDict 
f1=open (r"C:\Users\hyder\Desktop\advent calender\input day8test.txt",'r')
filename=f1.read() #reading in the file into a string
clean_file2=filename.replace("\n", " ") #removing white space
#clean_file2=clean_file.replace("->"," ")
clean_file2=clean_file2.replace("|"," ")
in_list_form=clean_file2.split(" ") #converting the whitespace-less string to a list
#in_list_form=clean_file
test_list = ' '.join(in_list_form).split()

arr=[]
for x in range(11):
    arr.append([])
    for y in range(4):
        arr[x].append([])
        for z in range(1):
            arr[x][y].append(0)
#print(arr)

carr=[]
for x in range(11):
    carr.append([])
    for y in range(10):
        carr[x].append([])
        for z in range(1):
            carr[x][y].append(0)

d1counter=0
d2counter=0
d3counter=0
d4counter=0

e1counter=0
e2counter=0
e3counter=0
e4counter=0
e5counter=0
e6counter=0
e7counter=0
e8counter=0
e9counter=0
e10counter=0

for item in range(len(test_list)):
    if item%14==0:
        carr[e1counter][0]=''.join(sorted(test_list[item]))
        e1counter+=1
    elif item%14==1:
        carr[e2counter][1]=''.join(sorted(test_list[item]))
        e2counter+=1
    elif item%14==2:
        carr[e3counter][2]=''.join(sorted(test_list[item]))  
        e3counter+=1
    elif item%14==3:
        carr[e4counter][3]=''.join(sorted(test_list[item]))
        e4counter+=1
    elif item%14==4:
        carr[e5counter][4]=''.join(sorted(test_list[item]))
        e5counter+=1
    elif item%14==5:
        carr[e6counter][5]=''.join(sorted(test_list[item]))
        e6counter+=1
    elif item%14==6:
        carr[e7counter][6]=''.join(sorted(test_list[item]))  
        e7counter+=1
    elif item%14==7:
        carr[e8counter][7]=''.join(sorted(test_list[item]))
        e8counter+=1
    elif item%14==8:
        carr[e9counter][8]=''.join(sorted(test_list[item]))
        e9counter+=1
    elif item%14==9:
        carr[e10counter][9]=''.join(sorted(test_list[item]))
        e10counter+=1

    elif item%14==10:
        arr[d1counter][0]=''.join(sorted(test_list[item]))
        d1counter+=1
    elif item%14==11:
        arr[d2counter][1]=''.join(sorted(test_list[item]))
        d2counter+=1
    elif item%14==12:
        arr[d3counter][2]=''.join(sorted(test_list[item]))  
        d3counter+=1
    elif item%14==13:
        arr[d4counter][3]=''.join(sorted(test_list[item]))
        d4counter+=1
print(arr)
print("hello")
print(carr)
#easycounter=0
zero=""
one=""
two=""
three=""
four=""
five=""
six=""
seven=""
eight=""
nine=""

s=0

for i in range(11):
    for item in carr[i]:
        if len(item)==2:
            one=item
        elif len(item)==4:
            four=item
        elif len(item)==3:
            seven=item
        elif len(item)==7:
            eight=item
        elif len(item)==5 and (0 not in [c in item for c in seven]):
            three=item
        elif len(item)==6 and (0 not in [c in item for c in seven]):
            if 0 not in [c in item for c in four]:
                nine=item
            else:
                zero=item
        elif len(item)==6:
            six=item
        temp=str(item)+four
        temp="".join(dict.fromkeys(temp))
        print(temp)
        if (temp==eight):
            two=item
        else:
            five=item
    print("one",one,"two",two,"three",three,"four",four,"five",five,"six",six,"seven",seven,"eight",eight,"nine",nine,"zero",zero)
    if arr[i][0]==zero:
        s=s+0
    elif arr[i][0]==one:
        s=s+1000
    elif arr[i][0]==two:
        s=s+2000
    elif arr[i][0]==three:
        s=s+3000
    elif arr[i][0]==four:
        s=s+4000
    elif arr[i][0]==five:
        s=s+5000
    elif arr[i][0]==six:
        s=s+6000
    elif arr[i][0]==seven:
        s=s+7000
    elif arr[i][0]==eight:
        s=s+8000
    elif arr[i][0]==nine:
        s=s+9000
    print(s)
    if arr[i][1]==zero:
        s=s+0
    elif arr[i][1]==one:
        s=s+100
    elif arr[i][1]==two:
        s=s+200
    elif arr[i][1]==three:
        s=s+300
    elif arr[i][1]==four:
        s=s+400
    elif arr[i][1]==five:
        s=s+500
    elif arr[i][1]==six:
        s=s+600
    elif arr[i][1]==seven:
        s=s+700
    elif arr[i][1]==eight:
        s=s+800
    elif arr[i][1]==nine:
        s=s+900

    if arr[i][2]==zero:
        s=s+0
    elif arr[i][2]==one:
        s=s+10
    elif arr[i][2]==two:
        s=s+20
    elif arr[i][2]==three:
        s=s+30
    elif arr[i][2]==four:
        s=s+40
    elif arr[i][2]==five:
        s=s+50
    elif arr[i][2]==six:
        s=s+60
    elif arr[i][2]==seven:
        s=s+70
    elif arr[i][2]==eight:
        s=s+80
    elif arr[i][2]==nine:
        s=s+90

    if arr[i][3]==zero:
        s=s+0
    elif arr[i][3]==one:
        s=s+1
    elif arr[i][3]==two:
        s=s+2
    elif arr[i][3]==three:
        s=s+3
    elif arr[i][3]==four:
        s=s+4
    elif arr[i][3]==five:
        s=s+5
    elif arr[i][3]==six:
        s=s+6
    elif arr[i][3]==seven:
        s=s+7
    elif arr[i][3]==eight:
        s=s+8
    elif arr[i][3]==nine:
        s=s+9
    
    print(s)

print(s)
#print(easycounter)