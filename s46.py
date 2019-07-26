def get_area(k):
    x = input("Enter the num:")
    add=[]
    for i in range(0,(len(k)-2),2):
        add.append(k[i]*k[i+3]-k[i + 1]*k[i + 2])
        add.append(k[len(k)-2]*k[1]-k[len(k) - 1]*k[0])
        return abs(sum(add)/2)
        print(get_area([4,10,9,7,11,2,2,2]))