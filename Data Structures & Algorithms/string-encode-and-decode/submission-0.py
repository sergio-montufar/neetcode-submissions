class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        length_of_string = 0
        for string in strs:
            length_of_string = len(string)
            encoded_string += f"{length_of_string}" + "#" + string
        
        print(encoded_string)
        return encoded_string


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            j = i + length
            ans.append(s[i:j])
            i = j
            

        return ans
