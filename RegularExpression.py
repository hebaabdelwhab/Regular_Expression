import re

txt = "هات دواء بنادوال" #V N TRP

def CheckStatement(Input):
    ret = re.match(r"V( )*(V?)( )*(D( )*N|D( )*TRP)*(N( )*|TRP( )*)(N*TRP*)(D( )*N|D( )*TRP)*(N|TRP)*",Input)
    print(ret)
    if ret:
      print("YES! We have a match!")
    else:
      print("No match")
Input = "V  N TRP"
CheckStatement(Input)