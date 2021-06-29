
n_str = input("Input an integer (0 terminates): ")

# Good stuff goes here
positive_int_count=0
odd_sum=0
even_sum=0
even_count=0
odd_count=0

while   n_str!="0":
        n_int =int(n_str)
    if  n_int < 0:
         n_str = input("It's negative,Input an integer again(0 terminates): ")
         continue
    elif n_int % 2==1:
         n_str = input("Input an integer (0 terminates): ")
         odd_sum+=n_int
         odd_count+=1
         positive_int_count+=1
         continue
    else：
         n_str = input("Input an integer (0 terminates): ")
         even_sum+=n_int
         even_count+=1
         positive_int_count+=1
         continue



    
    
    
    

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
