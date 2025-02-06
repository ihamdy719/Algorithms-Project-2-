def Birthday_cake(): 
    num_candles = int(input("How many candles To add it: ")) 
    height_candles = [] 
    for i in range(num_candles): 
        candle_per_height = int(input(f"Enter The height of The candle its position {i + 1}: ")) 
        height_candles.append(candle_per_height) 
    center = int((num_candles) / 2) 
    max_height = 0 
    count1 = 0 
    count2 = 0 
    for i in height_candles: 
        count1+=1 
    for i in range(count1): 
        if height_candles[i] > max_height: 
            max_height = height_candles[i] 
    if height_candles[center] == max_height: 
        print(f"The tallest candle is {max_height} and locate in The center = {center + 1}") 
        for i in range(count1): 
            if max_height == height_candles[i]: 
                count2+=1 
        print(f"number of tallest candle is {count2}") 
        j = 1 
        for i in range(center): 
            if num_candles % 2 != 0: 
                if height_candles[center - j] != height_candles[center + j]: 
                    return "Is symmetric: False" 
            else: 
                return "Is symmetric: False" 
            j+=1 
        return "Is symmetric: True" 
    else: 
        return "tallest candle must be in the center" 
print(Birthday_cake()) 




'''

Review of the Pseudocode 


Function Birthday: 
   Print("Enter the number of candles: ") 
   Read num_candles 
   Height candles                                 [] 
   Max height   0 
   Count1   0 
   Count2 0 
For each i to range (num_candles): 
    Do print (" Enter height of the candles:" ) 
    Read candle height 
    Add candle height to height candles  
     For each height to height candles: 
         Do if heigh < max_height then 
                    Max_height=height 
                     If height candles[center]==max_height  Then 
Print("the tallest candle is",max_height,"and located in the center",center) 
                      For each height to height candles: 
                           Do if height == max_height then  
                               Increment count2 
                       Print("number of tallest candles is",counter2) 
                        j 1 
                        for each i to range(center): 
                            do if num_candles %2 !=0 
                              then  if height candles [center-j]!=height candles[center+j]then 
                                                      return "Is symmetric:false " 
                                          else: 
                                                        return "Is symmetric:false " 
                                                         increment j 
                                                          return "Is symmetric:true  " 
print(birthday cake)



'''