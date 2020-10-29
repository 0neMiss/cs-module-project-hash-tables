
def has_negatives(list):

    # Your code here
    #if the list has a length
    if len(list) > 0:
        #populating the dictionary with the list with the iteration as the key: and the value at the index as the value
        dict = {i: list[i] for i in range(0 ,len(list))}
        print(dict)
        result = []
        neg_list = []
        for item in range(0, len(dict)):
            #set variable for the value at the index
            value = dict.get(item)

            if value <= 0:
                neg_list.append(value)


            else:
                print(value)
                #if the value at that index is greater than 0 calculate the negative version of that number
                num_neg = value - (value * 2)
                print(num_neg)
                #if that exists in the dictionary
                if num_neg in neg_list:
                    print(value)
                    #append to the result array
                    result.append(value)
                    print(result)

        return result
    else:
        return None

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
