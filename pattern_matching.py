import time
def BruteForce(text,pattern):
  count1=0
  n = len(text)
  m = len(pattern)
  for i in range(0,n-m+1):
    j =0
    while(j<m and text[i+j]==pattern[j]):
      j= j+1
      count1+=1
    if j==m:
      print("**********Brute Force**********")
      print("Number of comparisions for Brute Force :")
      print(count1)
      return i
    count1+=1
  print("**********Brute Force**********")
  print("Number of comparisions for Brute Force :")
  print(count1)
  return -1

def KMP(text,pattern):
  text_length = len(text)
  pattern_length = len(pattern)
  prefix_suffix_lst = [None]*pattern_length
  longest_prefix_suffix_lst = failure_function(pattern, pattern_length,prefix_suffix_lst)
  i=0
  j=0
  count2=0
  while(i<text_length):
    count2+=1
    if(text[i]==pattern[j]):
      if(j==pattern_length-1):
        print("********** KMP **********")
        print("Number of comparisions for KMP :")
        print(count2)
        return i-j
      else:
        i+=1
        j+=1
    elif(j>0):
      j= longest_prefix_suffix_lst[j-1]
    else:
      i+=1
  print("********** KMP **********")
  print("Number of comparisions for KMP :")
  print(count2)
  return -1

def failure_function(pattern,pattern_length,prefix_suffix_lst):
  j=0
  i=1
  prefix_suffix_lst[0]=0
  while(i<pattern_length):
    if(pattern[i]==pattern[j]):
      prefix_suffix_lst[i]=j+1
      j+=1
      i+=1
    elif(j>0):
      j=prefix_suffix_lst[j-1]
    else:
      prefix_suffix_lst[i]=0
      i+=1
  return prefix_suffix_lst

def horspool(text,pattern):
  text_length = len(text)
  pattern_length = len(pattern)
  shift_value = [None]*256
  count3=0
  for k in range(0,256):
    shift_value[k] = pattern_length
  for k in range(0,pattern_length-1):
    shift_value[ord(pattern[k])]=pattern_length-1-k
  i=0
  j=0
  while(i+pattern_length<=text_length):
    j=pattern_length-1
    while(text[i+j]==pattern[j]):
      j-=1
      count3+=1
      if(j<0):
        print("********** Horspool **********")
        print("Number of comparisions for Horspool :")
        print(count3)
        return i
    count3+=1
    i=i+shift_value[ord(text[i+pattern_length-1])]
  print("********** Horspool **********")
  print("Number of comparisions for Horspool :")
  print(count3)
  return -1

text = input("enter text :")
pattern = input("enter pattern :")
print("computing all algorithms")
start_time = time.time()
position1 = BruteForce(text,pattern)
if(position1 == -1):
  print("no match found for Brute Force")
else:
  print("position found at ")
  print(position1)
print("Run Time for Brute Force")
print((time.time()-start_time)*1000)
start_time = time.time()
position2 = KMP(text,pattern)
if(position2 == -1):
  print("no match found for KMP")
else:
  print("position found at ")
  print(position2)
print("Run Time for KMP")
print((time.time()-start_time)*1000)
start_time = time.time()
position3 = horspool(text,pattern)
if(position3 == -1):
  print("no match found for Horspool")
else:
  print("position found at ")
  print(position3)
print("Run Time for Horspool")
print((time.time()-start_time)*1000)
