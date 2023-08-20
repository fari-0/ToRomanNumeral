def solution(n):
    n2=n
    sayi = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roma = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman=[]
    index=0
    for a in sayi:
        while n>=a:
            n-=a
            roman.append(roma[index])
        index+=1
    roman="".join(roman)
    print(n2)
    print(roman)
    
solution(15)