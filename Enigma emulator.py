isnput1=0
intput2=0
rotor1=3
rotor2=1
rotor3=1
output=0
output2=0
output3=0
output4=0
while 1<2:
    input1=input("Letter")
    #kickover points
    if rotor1==26:
        rotor2=rotor2+1
        rotor1=1
    if rotor2==26:
        rotor3==rotor3+1
        rotor2=1
    if rotor3==26:
        print("Too much")
    #letter to number
    if input1=="a":
        input2=1
    if input1=="b":
        input2=2
    if input1=="c":
        input2=3
    if input1=="d":
        input2=4
    if input1=="e":
        input2=5
    if input1=="f":
        input2=6
    if input1=="g":
        input2=7
    if input1=="h":
        input2=8
    if input1=="i":
        input2=9
    if input1=="j":
        input2=10
    if input1=="k":
        input2=11
    if input1=="l":
        input2=12
    if input1=="m":
        input2=13
    if input1=="n":
        input2=14
    if input1=="o":
        input2=15
    if input1=="p":
        input2=16
    if input1=="q":
        input2==17
    if input1=="r":
        input2=18
    if input1=="s":
        input2=19
    if input1=="t":
        input2=20
    if input1=="u":
        input2=21
    if input1=="v":
        input2=22
    if input1=="w":
        input2=23
    if input1=="x":
        input2=24
    if input1=="y":
        input2=25
    if input1=="z":
        input2=26
    
    output2=input2+rotor1+rotor2+rotor3#rotors
    
    output4=27-output2#mirror
    output5=output4-rotor1-rotor2-rotor3#rotors
    rotor1=rotor1+1#advance rotor 1
    output3=output5%26#turn it into number that can be turned into a letter
    #number to letter
    if output3==1:
        output4="a"
    if output3==2:
        output4="b"
    if output3==3:
        output4="c"
    if output3==4:
        output4="d"
    if output3==5:
        output4="e"
    if output3==6:
        output4="f"
    if output3==7:
        output4="g"
    if output3==8:
        output4="h"
    if output3==9:
        output4="i"
    if output3==10:
        output4="j"
    if output3==11:
        output4="k"
    if output3==12:
        output4="l"
    if output3==13:
        output4="m"
    if output3==14:
        output4="n"
    if output3==15:
        output4="o"
    if output3==16:
        output4="p"
    if output3==17:
        output4="q"
    if output3==18:
        output4="r"
    if output3==19:
        output4="s"
    if output3==20:
        output4="t"
    if output3==21:
        output4="u"
    if output3==22:
        output4="v"
    if output3==23:
        output4="w"
    if output3==24:
        output4="x"
    if output3==25:
        output4="y"
    if output3==0:
        output4="z"
    print(output4)
        
    




