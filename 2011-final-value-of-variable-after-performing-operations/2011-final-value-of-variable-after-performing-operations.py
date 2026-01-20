class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X=0
        d = {'++X':1,
            'X++':1,
            '--X':-1,
            'X--':-1,'X':0}
        for i in operations:
            X+=int(d[i])
        return X
        