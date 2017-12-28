# #Read Input
N = int(input())

# #Looping through each set of inputs
for counter in range(N):
    val_input = input()
    px, py, qx, qy = [int(ele) for ele in val_input.split(" ")]
    
    # #Compute Distances
    print(((2*qx) - px), ((2*qy) - py))
    
    