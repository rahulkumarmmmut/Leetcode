class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a','e','i','o','u','A','E','I','O','U']
        listString = list(s)

        start = 0
        end = len(listString)-1

        while(start < end):
            while(start<end and listString[start] not in vow):
                start+=1

            while(end >start and listString[end] not in vow):
                end-=1

            temp = listString[start]
            listString[start] = listString[end]
            listString[end] = temp

            end-=1
            start+=1

        return ''.join(listString)       
