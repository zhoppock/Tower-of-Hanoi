def TowerOfHanoi(n , source, destination, auxiliary, counter):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        counter += 1
        return counter
    counter = TowerOfHanoi(n-1, source, auxiliary, destination, counter)
    print ("Move disk",n,"from source",source,"to destination",destination)
    counter += 1
    counter = TowerOfHanoi(n-1, auxiliary, destination, source, counter)
    return counter
         
# Driver code
n = input("Number of disks: ")
n = int(n)
counter = 0
counter = TowerOfHanoi(n,'A','B','C', counter)
# A, C, B are the name of rods

print("Number of moves made:", counter)
# Contributed By Dilip Jain