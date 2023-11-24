def get_num_array(n):
    return_array = []
    
    if(n<0):
        return []

    for i in range(0,n+1):
        return_array.append(i)
    
    return return_array
        
if __name__ == "__main__":
    print(get_num_array(10))
