# Inclusive and Exclusive Scan

def inclusive_scan(identity=None, array=None):
    N = len(array)
    result = [None for i in range(N)]
    
    result[0] = array[0]
    for i in range(1, N):
        result[i] = result[i-1] + array[i]

    return result


def exclusive_scan(identity=None, array=None):
    N = len(array)
    result = [None for i in range(N)]
    
    result[0] = identity
    for i in range(1, N):
        result[i] = result[i-1] + array[i-1]
                                           
    return result

def main():
    in_array = [13, -10, 9, 11, -12]
    print(f"Input: {in_array}")
    
    inclusive_res = inclusive_scan(array=in_array)
    print(f"Result--inclusive scan: {inclusive_res}")

    exclusive_res = exclusive_scan(0, in_array)
    print(f"Result--inclusive scan: {exclusive_res}")


if __name__ == "__main__":
    main()
