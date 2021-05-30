from typing import List
import collections

# 2021.05.23 | gomip | created


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class DiameterOfBinaryTree:
    def __init__(self):
        self.longest = 0

    def solution(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return -1

            # 왼쪽 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            print(node.val,":", left, right)
            # 가장 긴 경로
            self.longest = max(self.longest, left+right + 2)

            print('node', node.val, self.longest)
            # 상태값
            return max(left, right) + 1
        dfs(root)
        return self.longest
    

if __name__ == '__main__':
    input = TreeNode(1)
    input.left = TreeNode(2)
    input.left.left = TreeNode(4)
    input.left.right = TreeNode(5)
    input.right = TreeNode(3)

    temp = DiameterOfBinaryTree()
    ans = temp.solution(input)
    print(ans)