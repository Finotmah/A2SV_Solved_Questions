def Needle_in_a_Haystack():
    n = int(input())
    results = []
    for _ in range(n):
        
        s = input().strip()
        t = input().strip()
    
        s_count = [0] * 26
        t_count = [0] * 26
        
        for char in s:
            s_count[ord(char) - ord('a')] += 1
    
        for char in t:
            t_count[ord(char) - ord('a')] += 1

        possible = True
        
        for i in range(26):
            if t_count[i] - s_count[i] < 0:
                possible = False
                break
            else:
                t_count[i] = t_count[i] - s_count[i]

        if not possible:
            results.append("Impossible")
            possible = True
            continue

        diff_string = []
        for i in range(len(t_count)):
            diff_string.append(chr(i + ord('a')) * t_count[i])
        
        diff_string.sort()

        diff_string = ''.join(diff_string)
        
        i = 0
        j = 0
        shufled_string = ''
        
        while i < len(s) and j < len(diff_string):
            if s[i] <= diff_string[j]:
                shufled_string += s[i]
                i += 1
            
            else:
                shufled_string += diff_string[j]
                j += 1

        
        shufled_string += diff_string[j:]
        shufled_string += s[i:]
            
        results.append(shufled_string)

    for result in results:
        print(result)

if __name__ == "__main__":
    Needle_in_a_Haystack()
        

    
