def bsearch(data, target):
      low=0
      high=len(data)-1
      while low < high:
            mid = (low+high)//2;
            if  target== data[mid]:
                  return mid
            elif target < data[mid]:
                  high=mid-1
            elif target > data[mid]:
                 low=mid+1
      else:
            return None;
a=[1,6,9,15,17,20]
find=bsearch(a,17)
print(find)
