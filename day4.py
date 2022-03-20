
drawn_list=[94,21,58,16,4,1,44,6,17,48,20,92,55,36,40,63,62,2,47,7,46,72,85,24,66,49,34,56,98,41,84,23,86,64,28,90,39,97,73,81,12,69,35,26,75,8,32,77,52,50,5,96,14,31,70,60,29,71,9,68,19,65,99,57,54,61,33,91,27,78,43,95,42,3,88,51,53,30,89,87,93,74,18,15,80,38,82,79,0,22,13,67,59,11,83,76,10,37,25,45]
#drawn_list=[7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
#first we open the files we need.
f1=open (r"C:\Users\hyder\Desktop\advent calender\input day4.txt",'r')
filename=f1.read() #reading in the file into a string
clean_file=filename.replace("\n", " ") #removing white space
clean_file2=clean_file.replace(" "," ")
in_list_form=clean_file2.split(" ") #converting the whitespace-less string to a list
#in_list_form=clean_file
test_list = ' '.join(in_list_form).split()

#print(test_list)
#print(len(test_list))

n = 100
arr = []
for x in range(n):
    arr.append([])
    for y in range(5):
        arr[x].append([])
        for z in range(5):
            arr[x][y].append(0)
#print(arr)

index=0

for i in range(n):
    for j in range(5):
        for k in range(5):
            arr[i][j][k]=test_list[index]
            index+=1
#print(arr[13])
new_arr=[]
win=[False]*100
print(win[0])
#sprint("hello")
for item in drawn_list:
    #print(item)
    for i in range(n):
       if win[i]==False:
            for j in range(5):
                for k in range(5):
                    if int(arr[i][j][k])==int(item):
                        arr[i][j][k]=-1
                        if i==13:
                            print(item)
                        #print (item)

                    if int(arr[i][0][k])+int(arr[i][1][k])+int(arr[i][2][k])+int(arr[i][3][k])+int(arr[i][4][k])==-5:
                        #print (i)
                        new_arr.append(i)
                        #new_arr.append(i) if i not in new_arr else new_arr
                        win[i]=True
                        break


                if int(arr[i][j][0])+int(arr[i][j][1])+int(arr[i][j][2])+int(arr[i][j][3])+int(arr[i][j][4])==-5:
                    #print (i)
                    new_arr.append(i)
                    #new_arr.append(i) if i not in new_arr else new_arr
                    win[i]=True
                    break

 
            
#print(arr[13])
print(new_arr)

res = []
[res.append(x) for x in new_arr if x not in res]
print(res)
