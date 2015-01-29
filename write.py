text_file= open("testwrite.py", "w")
ifform=input("What do you want as the operator")
ifform2=input("What do you want it to equal")
ifform3=input("What do you want the limit of x and y to be")
ifstr="   if((x"+str(ifform)+"y) =="+str(ifform2)+"): \n"
elif1="   elif(x=="+str(ifform3) +"): \n"
elif2="   elif(y=="+str(ifform3) +"): \n"
text_file.write("x=0 \n")
text_file.write("y=0 \n")
text_file.write("z=0 \n")
text_file.write("while(z==0): \n")
text_file.write(ifstr)
text_file.write("      print(str(x) + 'and' + str(y)) \n")
text_file.write(elif1)
text_file.write("      x=0 \n")
text_file.write("      y=y+1 \n")
text_file.write(elif2)
text_file.write("      z=1 \n")
text_file.write("   x=x+1 \n")



text_file.close()
