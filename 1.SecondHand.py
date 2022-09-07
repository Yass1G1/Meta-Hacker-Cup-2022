# By Yassine Chouiti for Meta Hacker cup 2022

# to open a file as an input
with open("final_input_secondhand.txt") as f:
    lines = f.read().splitlines()


def full_test(num):

    line_counter = 0 # to count line as an index for the input line
    results = []

    # number of test case
    for i in range(int(num)):
        i += 1

        # Split N int and K int + input
        line_counter += 1
        nk_input = lines[line_counter]
        nk_list = nk_input.split(" ")

        # Split numbers
        line_counter += 1
        numbers = lines[line_counter]
        list_nums = numbers.split(" ")

        # Verify 3-occurence of numbers in the set
        three_occ = 0
        for j in list_nums:
                if list_nums.count(j) >= 3:
                    three_occ = 1

        # final verification
        if int(nk_list[0]) > (int(nk_list[1]) * 2) or three_occ == 1:
            results.append(0)
        else:
            results.append(1)
    

    outpt_file = open("output_secondhand_final.txt", "a")

    counter = 0 # for the case number
    print("\nSuccess !\n")
    for r in results:
        if r == 1:
            counter += 1
            outpt_file.write("Case #%d: YES\n" %counter)
        else:
            counter += 1
            outpt_file.write("Case #%d: NO\n" %counter)

    outpt_file.close()
    f.close()


    
            
            
full_test(lines[0])


