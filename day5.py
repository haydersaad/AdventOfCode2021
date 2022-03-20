#first we open the files we need.
f1=open (r"C:\Users\hyder\Desktop\advent calender\input day5test.txt",'r')
filename=f1.read() #reading in the file into a string
clean_file=filename.replace("\n", " ") #removing white space
clean_file2=clean_file.replace("->"," ")
clean_file2=clean_file2.replace(","," ")
in_list_form=clean_file2.split(" ") #converting the whitespace-less string to a list
#in_list_form=clean_file
test_list = ' '.join(in_list_form).split()

from_x_counter=0
from_y_counter=0

to_x_counter=0
to_y_counter=0

sum_arr=[]
for x in range(10):
    sum_arr.append([])
    for y in range(10):
        sum_arr[x].append([])
        for z in range(1):
            sum_arr[x][y].append(0)


n = 10 #500
from_arr = []
to_arr=[]
for x in range(n):
    from_arr.append([])
    for y in range(2):
        from_arr[x].append([])
        for z in range(1):
            from_arr[x][y].append(0)

for x in range(n):
    to_arr.append([])
    for y in range(2):
        to_arr[x].append([])
        for z in range(1):
            to_arr[x][y].append(0)

for i in range(len(test_list)):
    if i%4==0:
        from_arr[from_x_counter][0]=test_list[i]
        from_x_counter+=1
    if i%4==1:
        from_arr[from_y_counter][1]=test_list[i]
        from_y_counter+=1
    if i%4==2:
        to_arr[to_x_counter][0]=test_list[i]
        to_x_counter+=1
    if i%4==3:
        to_arr[to_y_counter][1]=test_list[i]
        to_y_counter+=1


for i in range(10):#500:
    if from_arr[i][0]==to_arr[i][0]:
        #print(from_arr[i][0])
        if int(from_arr[i][1])<(int(to_arr[i][1])):
            for y in range(int(from_arr[i][1]),(int(to_arr[i][1])+1)):
                sum_arr[y][int(from_arr[i][0])][0] +=1
        if int(from_arr[i][1])>(int(to_arr[i][1])):
            for y in range(int(to_arr[i][1]),(int(from_arr[i][1])+1)):
                sum_arr[y][int(from_arr[i][0])][0] +=1
        
    
    if from_arr[i][1]==to_arr[i][1]:
        #print(to_arr[i][1])
        if int(from_arr[i][0])<(int(to_arr[i][0])):
            for x in range(int(from_arr[i][0]),(int(to_arr[i][0])+1)):
                sum_arr[int(from_arr[i][1])][x][0]+=1
        if int(from_arr[i][0])>(int(to_arr[i][0])):
            for x in range(int(to_arr[i][0]),(int(from_arr[i][0])+1)):
                sum_arr[int(from_arr[i][1])][x][0]+=1

    if ((int(from_arr[i][1])-int(to_arr[i][1]))==(int(from_arr[i][0])-int(to_arr[i][0]))):
        if int(from_arr[i][1])>(int(to_arr[i][1])): #case when from (x,y) are bigger than to(x,y)
            y=int(to_arr[i][1]) 
            for x in range(int(to_arr[i][0]),(int(from_arr[i][0])+1)):
                sum_arr[y][x][0] +=1
                y+=1

        if int(from_arr[i][1])<(int(to_arr[i][1])): #case when from(x,y) are less than to(x,y) 
            y=int(from_arr[i][1])
            for x in range(int(from_arr[i][0]),(int(to_arr[i][0])+1)):
                sum_arr[y][x][0] +=1
                y+=1

    if ((int(from_arr[i][1])-int(to_arr[i][1]))==-1*(int(from_arr[i][0])-int(to_arr[i][0]))):
        if int(from_arr[i][1])>(int(to_arr[i][1])): #case when numerator pos i.e. from y>to y but from x<to x
            y=int(to_arr[i][1])
            for x in range(int(from_arr[i][0]),(int(to_arr[i][0])+1)):
                sum_arr[y][x][0] +=1
                y+=1

        if int(from_arr[i][1])<(int(to_arr[i][1])): #case when numerator neg i.e. from y<to y but from x>to x
            y=int(from_arr[i][1])
            for x in range(int(to_arr[i][0]),(int(from_arr[i][0])+1)):
                sum_arr[y][x][0] +=1
                y+=1

        


#print(len(test_list))
#print(to_arr)
#print(from_arr)
#print(sum_arr[210:250])
counter=0

for x in range(10):
    for y in range(10):
        if sum_arr[x][y][0]>=2:
            #print(x)
            #print(y)
            counter+=1

print(counter)
print(sum_arr)