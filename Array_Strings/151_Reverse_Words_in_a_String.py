class Solution:
    def reverseWords(self, s: str) -> str:

        List_String = s.split(" ")
        List_String = [word for word in List_String if word.strip()]
        start =  0
        end = len(List_String)-1
        while(end>start):
            temp = List_String[start]
            List_String[start] = List_String[end]
            List_String[end] = temp
            end -= 1
            start +=1
        return " ".join(List_String)
        
