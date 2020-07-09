if __name__ == '__main__':
    report = []
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        report+=[[name,score]]
        scores+=[score]

    second=sorted(list(set(scores)))[1]
    
    for x,y in sorted(report):
        if (second==y):
            print(x)
    
