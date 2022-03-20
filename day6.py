fishies=[2,5,2,3,5,3,5,5,4,2,1,5,5,5,5,1,2,5,1,1,1,1,1,5,5,1,5,4,3,3,1,2,4,2,4,5,4,5,5,5,4,4,1,3,5,1,2,2,4,2,1,1,2,1,1,4,2,1,2,1,2,1,3,3,3,5,1,1,1,3,4,4,1,3,1,5,5,1,5,3,1,5,2,2,2,2,1,1,1,1,3,3,3,1,4,3,5,3,5,5,1,4,4,2,5,1,5,5,4,5,5,1,5,4,4,1,3,4,1,2,3,2,5,1,3,1,5,5,2,2,2,1,3,3,1,1,1,4,2,5,1,2,4,4,2,5,1,1,3,5,4,2,1,2,5,4,1,5,5,2,4,3,5,2,4,1,4,3,5,5,3,1,5,1,3,5,1,1,1,4,2,4,4,1,1,1,1,1,3,4,5,2,3,4,5,1,4,1,2,3,4,2,1,4,4,2,1,5,3,4,1,1,2,2,1,5,5,2,5,1,4,4,2,1,3,1,5,5,1,4,2,2,1,1,1,5,1,3,4,1,3,3,5,3,5,5,3,1,4,4,1,1,1,3,3,2,3,1,1,1,5,4,2,5,3,5,4,4,5,2,3,2,5,2,1,1,1,2,1,5,3,5,1,4,1,2,1,5,3,5,2,1,3,1,2,4,5,3,4,3]

#fishies=[3,4,3,1,2]
rows, cols = (257, 9)
count_arr = [[0 for i in range(cols)] for j in range(rows)]

for fish in fishies:
    count_arr[0][fish]+=1

#print(count_arr)

for day in range (1,257):
    count_arr[day][0]=count_arr[day-1][1]
    count_arr[day][1]=count_arr[day-1][2]
    count_arr[day][2]=count_arr[day-1][3]
    count_arr[day][3]=count_arr[day-1][4]
    count_arr[day][4]=count_arr[day-1][5]
    count_arr[day][5]=count_arr[day-1][6]
    #count_arr[6]=0
    count_arr[day][6]=count_arr[day-1][7]+count_arr[day-1][0]
    #count_arr[day][6]+=count_arr[day-1][0]
    count_arr[day][7]=count_arr[day-1][8]
    count_arr[day][8]+=count_arr[day-1][0]
    #print("hello")
    #print(count_arr)

counter=0
for arr in count_arr[256]:
    counter+=arr

print(counter)

