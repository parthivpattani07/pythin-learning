code1='tuud rrra eeit sbex'
code2='TETOIUIN HBOBNTRO EETETYDW FLHLHORA UOOIEFEN TNSEBTAD UGWVEHMF RSHEAESX'

def caesar_box(code,size):       # size is always squre root of total letters.

    code=code.replace(" ","")
    code_0=code[0::size]+ code[1::size]+ code[2::size]+code[3::size]
    if not isinstance(size,int):
        return 'size should be an integer '
    
    return code_0 +" "+ "The code is decihpherd and now breaking it into words will give us the hidden message." 


print(caesar_box(code1,4))
print(caesar_box(code2,8))

output:  tresureburiedatx 
        The code is decihpherd and now breaking it into words will give us the hidden message.  # tresure buried at x
        THEFUTUREBELONGSTOTHOSEWHOBELIEVE
        The code is decihpherd and now breaking it into words will give us the hidden message.  # THE FUTURE BELONGS TO THOSE WHO BELIEVE
