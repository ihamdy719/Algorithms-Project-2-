def dominator():     
    count1 = 0 
    my_list = [] 
    numbers = int(input("How many to add it: ")) 
    for i in range(numbers): 
        num = int(input(f"my_list [{i}]: ")) 
        my_list.append(num) 
    for i in range(numbers): 
        count1+=1 
    half_len = count1 / 2 
    count2 = 0 
    dom_list = [] 
    for i in range(numbers): 
        for j in range(numbers): 
            if my_list[i] == my_list[j]: 
                count2+=1 
                dom_list.append(j) 
        if count2 > half_len: 
            return dom_list             
        else: 
            count2 = 0 
            dom_list.clear() 
    return -1 
print(dominator())





'''


function dominator: 
    count1                   0 
    my_list                  [] 
    print("How many to add it: ") 
    read numbers 
    for i to range(numbers) do 
        print(f"my_list[{i}]: ") 
        read num 
        insert num into list my_list 
    for i to range(numbers) do 
        count1                count1 + 1 
    half_len                   count1 / 2 
    count2                      0 
    dom_list                   [] 
    for i to range(numbers) do 
        for j to range(numbers) do 
            if my_list[i] == my_list[j] Then 
                count2                     count2 + 1 
                insert j into list dom_list 
        if count2 > half_len Then 
            return dom_list 
        else 
            count2                0 
            dom_list.clear() 
    return -1 
print(dominator)




'''