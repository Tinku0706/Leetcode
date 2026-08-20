class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        j=len(s)
        while i<j and s[i]==' ': #skip leading space
            i+=1
        sign=1
        if i<j and s[i]=='-': #skip signs and comit to one sign
            sign=-1
            i+=1
        elif i<j and s[i]=='+':
            i+=1
        num=0
        while i<j and s[i].isdigit():#keep on adding num untill end or char appears
            num=num*10+(int(s[i]))
            i+=1
        num=num*sign
        if num<-2**31:
            return -2**31
        if num>2**31-1:
            return 2**31-1
        return num
    #Normally, Python integers have no practical size limit (other than available memory).x = 999999999999999999999999999999999999999999 Python handles it fine.
    #A 32-bit signed integer uses 32 bits:1 bit for sign (+/-) 31 bits for value
     #Python integers can grow arbitrarily large, but myAtoi follows the problem requirement of returning a signed 32-bit integer, whose range is [-2^31, 2^31 - 1] = [-2147483648, 2147483647].

     #"91283472332"->Converted number:->91283472332=>But this is larger than 2147483647
     #So return:  2147483647
     #"-91283472332"->Converted number:->91283472332=>But this is larger than -2147483648
     #So return:  -2147483648

