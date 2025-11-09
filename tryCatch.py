# 1> program to open non-existence file
# def exceptionHandling():
#     try:
#         f=open('temporary_file','r')
#     except IOError:
#         print('error with opening the file') 
#     print('program continues smoothly even after error')
# exceptionHandling()        
# 2>
# import sys
# def main():
#     try:
#         f=open('temporay_file','r')

#     except IOError as err:
#         print('error with opening the file \n',err)
#         print()
#         print(sys.exc_info())
#     print('program continues smoothly even after error')
# main()        

# 3> program to compute price per unight weight of an item    
# import sys
# def pricePerWeight():
#     price=input('enter price of an item purchased :') 
#     weight=input('enter weight of item purchased  :')
#     try:
#      if price==" ":
#          price=None
#      if weight==" ":
#         price=None
#      price=float(price)
#      weight=float(weight)    
#      assert price>=0 and weight>=0
#      result=price/weight
#     except(ValueError,TypeError,AssertionError,ZeroDivisionError):
#        print("wrong input provided by users: \n"+str(sys.exc_info()))
#     else:
#        print(f"price per unight weight is:  {result} ")  
# pricePerWeight() 
 
#4> Same above program with multiple except block
import sys
def pricePerWeight():
    price=input("enter price of an item purchased :")
    weight=input("enter weight of the item purchased: ")
    try:
        if price==" ":
            price=None
        if price==" ":
            price=None
        price=float(price)
        weight=float(weight)
        assert price>=0 and weight>=0
        result=price/weight
    except ValueError:
        print("wrong input : ValueError")
    except TypeError:
        print("wrong inputs : TypeError")
    except AssertionError:
        print("wrong inputs : AssertionError")
    except ZeroDivisionError:
        print("wrong inputs : ZeroDivisionError")
    except:
        print(str(sys.exc_info()))
    else:
        print(f"Price per unight weight is: {result}") 
         
pricePerWeight()        


        