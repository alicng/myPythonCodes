def turn_calc(num):

    d={1:'I', 2:'Z', 3:'E', 4:'H', 5:'S', 6:'G', 7:'L', 8:'B', 9:'-', 0:'O'}
    
    return ''.join([d[x] for x in str(num)[::-1] if x != '.'])

a=turn_calc(5508)
print (a)
#[d[i] for i in str(num) if i not in d.keys() ]