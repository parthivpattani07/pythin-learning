code1='tuud rrra eeit sbex'
code2='TETOIUIN HBOBNTRO EETETYDW FLHLHORA UOOIEFEN TNSEBTAD UGWVEHMF RSHEAESX'

def caesar_box(code):  
    code=code.replace(" ","")
    size=int(len(code)**0.5)
    if not isinstance(size,int):
        return 'Size should be an integer. '
    code_0=code[0::size]+ code[1::size]+ code[2::size]+code[3::size]
    
    
    return code_0 +" "+ "The code is decihpherd and now breaking it into words will give us the hidden message." 
"""
input:
print(caesar_box(code1))
print(caesar_box(code2))
output:
trsureburiedatx The code is decihpherd and now breaking it into words will give us the hidden message.
FUTUREBELONGSTOTHOSEWHOBELIEVE The code is decihpherd and now breaking it into words will give us the hidden message.
"""

