# #first we open the files we need.
f1=open (r"C:\Users\hyder\Desktop\advent calender\input day2.txt",'r')
filename=f1.read() #reading in the file into a string
clean_file=filename.replace("\n", " ") #removing white space
in_list_form=clean_file.split(" ") #converting the whitespace-less string to a list
in_list_form.pop() #to remove the space that appears after the last word
#print(in_list_form)

#in_list_form=['forward', '5', 'down', '5','forward', '8', 'up', '3', 'down', '8', 'forward', '2',]


depth=0
horizontal=0
aim=0

for item in range(len(in_list_form)-1):
    if item%2==0:
        if in_list_form[item]=="forward":
            horizontal+=int(in_list_form[item+1])
            depth+=aim*int(in_list_form[item+1])
        elif in_list_form[item]=="down":
            aim+=int(in_list_form[item+1])
        elif in_list_form[item]=="up":
            aim-=int(in_list_form[item+1])
    else:
        continue

print(depth)
print(horizontal)
print(depth*horizontal)

