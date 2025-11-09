# 1> program to illustrate the use of raise and finally

def checkMarks():
    marks=110
    try:
      if marks<0 or marks>100:
        raise ValueError("marks should be b/w 0 and 100") 
    finally:
       print("bye")
    print("program continues after handling exception")
checkMarks()    

# 2> program to illustrate the use of raise and finally
def checkMarks():
    marks=110
    try:
      if marks<0 or marks>100:
        raise ValueError("marks should be b/w 0 and 100")
    except:
       pass  
    finally:
       print("bye")
    print("program continues after handling exception")
checkMarks()    
