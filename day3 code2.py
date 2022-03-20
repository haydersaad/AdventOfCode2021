# #first we open the files we need.
f1=open (r"C:\Users\hyder\Desktop\advent calender\input day3.txt",'r')
filename=f1.read() #reading in the file into a string
clean_file=filename.replace("\n", " ") #removing white space
in_list_form=clean_file.split(" ") #converting the whitespace-less string to a list
in_list_form.pop() #to remove the space that appears after the last word
#print(in_list_form)

#n_list_form=['00100', '11110', '10110', '10111','10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
new_list=[]
def o2_function(list,pos,new_list):
    new_list=[]
    sum=0
    for item in list:
        sum+=int(item[pos])
    #print(sum)
    if sum>=len(list)/2:
        for item in list:
            if int(item[pos])==1:
                new_list.append(item)
    else:
        for item in list:
            if int(item[pos])==0:
                new_list.append(item)
    
    if len(new_list)==1:
        return new_list
    else:
        #print(new_list)
        #print(pos)
        return o2_function(new_list,pos+1,new_list)

def co2_function(list,pos,new_list):
    new_list=[]
    sum=0
    for item in list:
        sum+=int(item[pos])
    #print(sum)
    if sum>=len(list)/2:
        for item in list:
            if int(item[pos])==0:
                new_list.append(item)
    else:
        for item in list:
            if int(item[pos])==1:
                new_list.append(item)
    
    if len(new_list)==1:
        return new_list
    else:
        #print(new_list)
        #print(pos)
        return co2_function(new_list,pos+1,new_list)

print(o2_function(in_list_form,0,new_list))
print(co2_function(in_list_form,0,new_list))




