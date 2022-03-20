
#first we open the files we need.
f1=open (r"C:\Users\hyder\Desktop\advent calender\input.txt",'r')
filename=f1.read() #reading in the file into a string
clean_file=filename.replace("\n", " ") #removing white space
in_list_form=clean_file.split(" ") #converting the whitespace-less string to a list
in_list_form.pop() #to remove the space that appears after the last word
#print(in_list_form)

#in_list_form=[199,200,208,210,200,207,240,269,260,263] #for q1

#in_list_form=[607,618,618,617,647,716,769,792] #for q2
#temp=in_list_form[0]
counter=0

temp=int(in_list_form[0])+int(in_list_form[1])+int(in_list_form[2])

for item in range(len(in_list_form)-2):
    sum=0
    sum=int(in_list_form[item])+int(in_list_form[item+1])+int(in_list_form[item+2])
    if sum>temp:
        counter+=1
    temp=sum

print(temp)
print(counter)

