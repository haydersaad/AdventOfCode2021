# #first we open the files we need.
f1=open (r"C:\Users\hyder\Desktop\advent calender\input day3.txt",'r')
filename=f1.read() #reading in the file into a string
clean_file=filename.replace("\n", " ") #removing white space
in_list_form=clean_file.split(" ") #converting the whitespace-less string to a list
in_list_form.pop() #to remove the space that appears after the last word
#print(in_list_form)

#in_list_form=['00100', '11110', '10110', '10111','10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']

sum_digits=[0,0,0,0,0,0,0,0,0,0,0,0]
gamma_list=[0,0,0,0,0,0,0,0,0,0,0,0]

#sum_digits=[0, 0, 0, 0, 0]
#gamma_list=[0, 0, 0, 0, 0]


gamma=0
sum=0


for item in in_list_form:
    for i in range(len(item)):
        sum_digits[i]+=int(item[i])

for item in sum_digits:
    for i in range(len(sum_digits)):
        if (sum_digits[i])>=(len(in_list_form)/2):
            gamma_list[i]=1

for i in range(len(gamma_list)):
    gamma+=int((gamma_list[11-i]))*(2**i)
print(sum_digits)
print(gamma_list)
print(gamma)
epsilon=4095-gamma
print(epsilon*gamma)

