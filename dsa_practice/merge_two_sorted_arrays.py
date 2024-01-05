def merge_two_sorted_arrays(list_m, m, list_n, n):
    for idx in range(n):
        list_m[m+idx] = list_n[idx]
    list_m.sort()
    
    print(list_m)
     
merge_two_sorted_arrays([1,2,3,0,0,0], 3, [2,5,6], 3)