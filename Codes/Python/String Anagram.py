def stringAnagram(dictionary, query):
    # Write your code here
    output=[]
    count = 0
  

    for q in query:
        for dic in dictionary:
            if(sorted(q)==sorted(dic)):
                count=count+1
        output.append(count)
        count=0
    return output

dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
query = ['codl', 'heater', 'abcd']

print(stringAnagram(dictionary, query))