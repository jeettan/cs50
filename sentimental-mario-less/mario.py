import cs50

N = 0

while(N < 1 or N>8):
    N = cs50.get_int("Height: ")

for i in range(0, N):
    for j in range (0, N):
        if(j < N-i-1):
            print("", end =" ")
        else:
            print("#", end ="")
    print()

