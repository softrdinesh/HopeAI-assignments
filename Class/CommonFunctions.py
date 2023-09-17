class CommonFunctions():
    def Subfields(fields):
        for temp in fields:
            print(temp)
          
    def OddEven(num):
        if(num%2==0):
            return str(num)+" is Even number"
        else:
            return str(num)+" is Odd number"
        
        
    def Eligible(gender,age):
        if((gender.upper()=="MALE" and age>=21) or(gender.upper()=="FEMALE" and age>=18)):
               return "Eligible"
        else:
                return "Not Eligible"
            
    def percentage(lst):
    
        total=0
        for temp in lst:
            total=total+temp
            return total
        
    def trianglearea(height,breadth):
        return (height*breadth)/2
    
    def TriangePermeter(height1,height2,breadth):
        return (height1+height2+breadth)