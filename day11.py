#list=[[[5],[4],[8],[3],[1],[4],[3],[2],[2],[3]],[[2],[7],[4],[5],[8],[5],[4],[7],[1],[1]],[[5],[2],[6],[4],[5],[5],[6],[1],[7],[3]],]

f1=open (r"C:\Users\hyder\Desktop\advent calender\input day11test.txt",'r')
filename=f1.read() #reading in the file into a string
clean_file=filename.replace("\n", " ") #removing white space
in_list_form=clean_file.split(" ") #converting the whitespace-less string to a list
#in_list_form.pop() #to remove the space that appears after the last word
print(in_list_form)

def explosion(arr,row,col):
    if arr[row][col]==10:
        arr[row][col]=0
        try:
            arr[row-1][col]+=1
            if arr[row-1][col]==10:
                explosion(arr,row-1,col)
        except:
            pass
        try:
            arr[row+1][col]+=1
            if arr[row+1][col]==10:
                explosion(arr,row+1,col)
        except:
            pass
        try:
            arr[row][col-1]+=1
            if arr[row][col-1]==10:
                explosion(arr,row,col-1)
        except:
            pass
        try:
            arr[row][col+1]+=1
            if arr[row][col+1]==10:
                explosion(arr,row,col+1)
        except:
            pass
        try:
            arr[row-1][col-1]+=1
            if arr[row-1][col-1]==10:
                explosion(arr,row-1,col-1)
        except:
            pass
        try:
            arr[row+1][col+1]+=1
            if arr[row+1][col+1]==10:
                explosion(arr,row+1,col+1)
        except:
            pass
        try:
            arr[row-1][col+1]+=1
            if arr[row-1][col+1]==10:
                explosion(arr,row-1,col+1)
        except:
            pass
        try:
            arr[row+1][col-1]+=1
            if arr[row+1][col-1]==10:
                explosion(arr,row+1,col-1)
        except:
            pass



n = 10
arr = []
for x in range(n):
    arr.append([])
    for y in range(10):
        arr[x].append([])
        for z in range(1):
            arr[x][y].append(0)

#print(arr)
for item in in_list_form:
    for i in range(len(item)):
        arr[in_list_form.index(item)][i]=int(item[i])

#print(arr)

for i in range(11):
    for row in range(10):
        for col in range(10):
            arr[row][col]+=1
            explosion(arr,row,col)
    print(arr)
