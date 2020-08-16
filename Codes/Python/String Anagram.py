def stringAnagram(dictionary, query):
    # Write your code here
    output=[]
    count = 0
  

    for i in range(0,len(dictionary)):
        dictionary[i] = sorted(dictionary[i])

    for q in query:
        count=dictionary.count(sorted(q))
        output.append(count)
        
    return output

dictionary = ['heater', 'cold', 'clod', 'reheat', 'docl']
query = ['codl', 'heater', 'abcd']

print(stringAnagram(dictionary, query))