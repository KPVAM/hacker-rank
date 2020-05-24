def kangaroo(x1, v1, x2, v2):
        
    if (x1>x2 and v2 <= v1) or (x2>x1 and v1 <= v2):
        print('NO')
    elif (x1==x2 and v1==v2):
        print("YES")
    
    elif  (abs(x1-x2)) % (abs(v1-v2)) == 0:
        print("YES")
    else:
        print("NO")
