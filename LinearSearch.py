#Linear Search in indexed interables - Lists, Tuples, Sets

arr = [2,10,8,0,-4,72,37,10,-3,10,2,3,4,8]

x = 8

def linearSearch(arr,x):
    if (arr.count(x)==1):
        return (arr.index(x))
    elif x not in arr:
        print ('Element does not exist')
    elif (arr.count(x)>1):
        inds = [i for i in range(len(arr)) if arr[i]==x]
        return (inds)


#'''
# Sample code to perform I/O:

#name = input()          # Reading input from STDIN
#print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
#'''

def choose_max(intel_levels):
    seq_ordered = sorted(intel_levels)
    break_points = []
    for I in range(len(seq_ordered)-1):
        if (abs(seq_ordered[I]-seq_ordered[I+1])>1):
            break_points.append(I)
            
    if break_points==[]:
        return (len(intel_levels))
        
    elif len(break_points)==1:
        f = len(intel_levels[:break_points[0]+1])
        s = len(intel_levels[break_points[0]+1:])
        return (max(f,s))
        
    elif len(break_points)>1:
        sub_seq_len = []
        for b in range(len(break_points)-1):
            sub_seq_len.append(len(intel_levels[break_points[b]+1:break_points[b+1]+1]))
        sub_seq_len.append(len(intel_levels[:break_points[0]+1]))
        sub_seq_len.append(len(intel_levels[break_points[0]+1:]))
        return (max(sub_seq_len))
            
            
if __name__ == '__main__':
    
    T = int(input())
    for t in range(T):
        N = int(input())
        intelligence_levels = list(map(int,input().strip().split()))
        print (choose_max(intelligence_levels))
    
