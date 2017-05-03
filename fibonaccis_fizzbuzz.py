#Kunal Gautam
#Codewars : @Kunalpod
#Problem name: Fibonacci's FizzBuzz
#Problem level: 7 kyu

def fibs_fizz_buzz(n):
    arr=[1,1]
    if n==1:
        return [1]
    for i in range(2,n):
        arr.append(arr[i-1]+arr[i-2])
    for i in range(2,n):
        if arr[i]%3==0 and arr[i]%5==0:
            arr[i]="FizzBuzz"
        elif not arr[i]%3:
            arr[i]="Fizz"
        elif not arr[i]%5:
            arr[i]="Buzz"
    return arr
