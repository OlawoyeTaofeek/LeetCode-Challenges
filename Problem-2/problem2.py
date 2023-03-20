def CalPoint(opp):
    output = []
    checks = True
    
    # check if operations constraints is met
    if  not (len(opp) >= 1 or len(opp) <= 1000):
        checks = False
            
    # check if '+' contraint is met
    for i in range(0, len(opp)):
        if (opp[i] == '+' and (i <= 1)):
            checks = False
    
    # check if 'C', 'D' contraint is meet
    for i in range(0, len(opp)):
        if ((opp[i] == 'C' or opp[i] == "D") and (i < 1)):
            checks = False
    
    if checks:
        # output.append(int(opp[0]))
        
        for i in range(0, len(opp)):
            if (opp[i] != "C" and opp[i] != "D" and opp[i] != "+"):
                output.append(int(opp[i]))
                
            if (opp[i] == "C"):
                output.remove(output[len(output) - 1])
                
            if (opp[i] == "D"):
                output.append(output[len(output) - 1] * 2)
                
            if (opp[i] == "+"):
                output.append(output[len(output) - 1] + output[len(output) - 2])
            
    total = 0
    for i in range(0, len(output)):
        total = output[i] + total 
    return total       


opp1 = '5 2 C D +'.split(" ")  
opp2 = '5 -2 4 C D 9 + +'.split(" ")  #:Satisfied

opp3 = '1'  #:Satisfied
print(CalPoint(opp1))
print(CalPoint(opp2))
print(CalPoint(opp3))
    
        
        
        
        
        


    # for i in range(0, len(opp)):
    #     if not ((int(opp[i])*1 >= (-3*104)) or (int(opp[i])*1 <= (3*104)) or 
    #             (opp[i] == '+') or (opp[i] == 'C') or (opp[i] == 'D')):
    #         checks  = False