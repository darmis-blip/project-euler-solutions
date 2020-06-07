max = 1

def get_digit_sum(n):
    sum = 0
    while(n!=0):
        sum+=n%10
        n=n//10
    return sum

for i in range(1,100):
    for j in range(1,100):
        k = get_digit_sum(i**j)
        if k>max:
            max = k
            print(i,j,k)
print(max)
