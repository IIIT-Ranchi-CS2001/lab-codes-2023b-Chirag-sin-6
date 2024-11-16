def mamax(lst):
    mx = -99999
    for i in lst:
        if i > mx:
            mx = i
    return mx

print(mamax([12,223,33434,345,545])) 