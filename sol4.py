def plusOne(digits):
    n = len(digits)
    

    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
        
            digits[i] += 1
            return digits
        else:
    
            digits[i] = 0
    
    
    return [1] + digits

# Driver code
digits = [1, 2, 3]
result = plusOne(digits)
print(result)