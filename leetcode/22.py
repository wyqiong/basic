# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []  

        def dfs(ans, right, left,path):
            if right==0 and left==0:
                result.append(path)
                return
            
            if left>0:
                dfs(ans,right,left-1,path+'(')
            # 那什么时候添加右括号呢？当左括号个数大于右括号的个数时添加右括号。
            if right>left:
                dfs(ans,right-1,left,path+')')

        dfs(result,n,n,'')
        return result