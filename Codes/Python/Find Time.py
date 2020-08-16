import timeit 
mysetup = ""
mycode = '''
def stringAnagram(dictionary, query):
    # Write your code here
    output=[]
    count = 0
  
 
    for i in range(0,len(query)):
        for j in range(0,len(dictionary)):
            if(sorted(query[i])==sorted(dictionary[j])):
                count=count+1
        output.append(count)
        count=0
 
    return output

dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
query = ['codl', 'heater', 'abcd']
'''

print(timeit.timeit(setup = mysetup,stmt = mycode, number = 1))