import os,sys
import pyautogui as pp
 
direct={}
consolidated={}
similar_name={}
count=0
space_conserved=0
# pathh=os.getcwd()
pathh=os.walk("/home/mandar/Desktop/MAin")
threshold=pp.prompt(text='Enter the threshold value', title='Linkpy' , default='')
# threshold=int(input("Enter the threshold value:(bytes) "))
threshold=0 #given 1Mb so 1024 bytes
for path,dirs,files in pathh:
   for i in files:               
       if i in direct:
           size=os.path.getsize(path+"/"+i)
          
           if os.path.getsize(direct[i]) == size and os.path.getsize(direct[i])>threshold:
               consolidated[i]=size,direct[i]
               os.remove(path+"/"+i)
               os.link(direct[i],path+"/"+i)
               space_conserved=space_conserved+size
              
           else:
               similar_name[path]=i
 
       if i not in direct:
           direct[i]=path+"/"+i
 
file=open("/home/mandar/Desktop/MAin/report.txt","w")
file.write("File Name \t\tFile Size \t\tHardlinked To\n")
for i in consolidated:
   file.write(i+"\t\t"+str(consolidated[i][0])+"\t\t"+consolidated[i][1]+"\n")
print("\n")
file.write("Total Space conserved is: "+str(space_conserved)+"bytes\n")
if len(similar_name)>0:
   file.write("Files with Similar name :\n")
   for key,value in similar_name.items():
       file.write(key +"\t")
       file.write(str(value))
       file.write("\n")
file.close()
