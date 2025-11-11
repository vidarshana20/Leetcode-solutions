class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        write = 0
        n = len(chars)

        while i < n:
            ch = chars[i]
            count = 0

            # count this consecutive group only
            while i < n and chars[i] == ch:
                i += 1
                count += 1

            # write the character
            chars[write] = ch
            write += 1

            # write the count (split into digits) if > 1
            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1

        return write

# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         inputarr=[]
#         i=0
#         while i < len(chars):
#             c=chars.count(chars[i])
    
#             if c==1:
#                 inputarr.append(chars[i])
#             elif c>1 and c<10:
#                 inputarr.extend([chars[i],c])  
#             elif c>10:
#                 a, b = map(int, str(c))
#                 inputarr.extend([chars[i], a, b])
#             i+=c
        
#         return(len(inputarr))

        