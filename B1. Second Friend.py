# By Yassine Chouiti for Meta Hacker Cup 2022

with open("second_friend_input_practice2.txt") as f:
    lines = f.read().splitlines()


def full_test(num):

    results = [] # results list to store "1" for "Possible" or "0" for "Impossible"
    lcount = 1 # Counter for line search

    outpt_file =  open("auto_result_secondfriend_practice.txt", "a")

    for i in range(int(num)):
        i += 1 # to start counter at 1
        
        rc_out = [int(x) for x in lines[lcount].split()] # takes Rows and Column int and split them into list
        lcount += 1
        rows, columns = rc_out[0], rc_out[1] # save rows and column into variable
        
        trees = [] # stores the forest

        # Pre-verification for "Case #i: Possible/impossible"
        for r in lines[lcount:lcount + rows]:
            if rows != 1 and columns != 1:
                outpt_file.write("Case #%d: Possible\n" %i) # 1
                # print("Case #%d: Possible\n" %i)
                break;
            elif rows != 1 and columns == 1:
                if r != "^":
                    outpt_file.write("Case #%d: Possible\n" %i) # 1
                    # print("Case #%d: Possible\n" %i)
                    break;
                else:
                    outpt_file.write("Case #%d: Impossible\n" %i)
                    # print("Case #%d: Impossible\n" %i)
                    break;

            elif rows == 1 and columns == 1:
                if r != "^":
                    outpt_file.write("Case #%d: Possible\n" %i) # 1
                    # print("Case #%d: Possible\n" %i)
                    break;
                else:
                    outpt_file.write("Case #%d: Impossible\n" %i)
                    # print("Case #%d: Impossible\n" %i)
                    break;
            else:
                outpt_file.write("Case #%d: Impossible\n" %i)
                # print("Case #%d: Impossible\n" %i)
                break;

     
        # Verification to display forest
        for r in lines[lcount:lcount + rows]:
            if rows != 1:
                # print("Plusieurs lignes")
                if columns == 1 and "^" in r == False:
                    # print("1 colonne et pas d\'arbre")
                    outpt_file.write(r + "\n")
                    results.append(1)
                elif columns == 1:
                    # print("1 seul colonne")
                    results.append(0)
                else: # 1
                    # print("plusieurs ligne et plusieurs colonnes")
                    outpt_file.write(r.replace(".", "^") + "\n")
                    results.append(1)
            elif rows == 1 and columns == 1:
                # print("1 seul colonne et une seul ligne")
                if r == "^":
                    results.append(0)
                else:
                    results.append(1)
                    outpt_file.write(r + "\n")
            else:
                # print("1 seul ligne")
                if columns != 1 and "^" in trees == False:
                    # print("1 seul ligne et plusieurs colonnes sans arbres")
                    outpt_file.write(r + "\n")
                    results.append(1)
                else:
                    # print("1 seul ligne et plusieurs colonnes")
                    results.append(0)
            lcount += 1

    outpt_file.close()
       
f.close()         
        

        


full_test(lines[0])