def permute_str(str):
    arr = []
    permutation(arr, str, "", len(str))
    return arr

def permutation(arr, str, config, size):
    
    if (not str and len(config) == size):

        print("adding: ", config)
        arr += [config]

    else:

        for i in range(len(str)):
            
            new_config = config # you must make a copy of the configuration!
            #otherwise you are adding to the same configuration!
            new_config += str[i]
            new_str = str[0:i] + str[i+1:]

            print("case: config-", new_config, "new_str-", new_str)

            permutation(arr, new_str, new_config, size)

arr = permute_str("abc")
print(arr)
