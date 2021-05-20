'''
5/10/2021
list is only 4 elements
mylist = [1,2,3,4]
reverse(mylist)

This need to return:
4,3,2,1


def reverse(l):
  x=[l[3], l[2], l[1], l[0]]
  return x

## test
mylist = [1,2,3,4]
newlist = reverse(mylist)
print(str(newlist)) 
'''
## reverse_no_limit
def reverse_no_limit(l):
  x = len(l)
  #lastindex = len(l) - 1
  lastindex = x - 1
  #print("Length of the list is " + str(x) + str(lastindex))

  nlist = []
  nindex = 0
  last_index = len(l) - 1
  #for y in range(last_index,-1,-1):
    #val = l[y]
    #print("val is: " + str(val))
    #print("nindex is: " + str(nindex))
    #nlist[nindex] = y+2
    #nindex += 1
    #nlist[nindex] = y

    ## Assign last value of list nlist to y:

 # for y in l:
 #   if(int(y) > 5):
 #   print("T")
 #     return True
 #   else:
 #     print("F")
 #     return False

  count = 0
  while(count <= len(l)-1):
    if(int(l[count]) > 5):
      print("T")
      return True
    count += 1
  else:
    print("F")
    return False


    
   

mylist = input("Please enter list: ")
#newlist = reverse_no_limit(mylist)
reverse_no_limit(mylist)