class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "0:empty"
        s="\n".join(strs)
        return s
    
    def decode(self, s: str) -> List[str]:
        if (s=="0:empty"):
            return []
        strs=s.split('\n')
        return strs
