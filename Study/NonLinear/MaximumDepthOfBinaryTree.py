from typing import List
import collections

# 2021.05.19 | gomip | created
# 이진 트리의 최대 깊이 구하기
# input = [3,9,20,None,None,15,7]
# output = 3


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximumDepthOfBinaryTree:
    def solution(self, root: TreeNode) -> int:
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            print(len(queue))
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                print('cur', cur_root.val)
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth


if __name__ == '__main__':
    input = [3, 9, 20, None, None, 15, 7]
    initTree = TreeNode(3)
    initTree.left = TreeNode(9)
    initTree.left.left = TreeNode(None)
    initTree.left.right = TreeNode(None)
    initTree.right = TreeNode(20)
    initTree.right.left = TreeNode(15)
    initTree.right.right = TreeNode(7)

    temp = MaximumDepthOfBinaryTree()
    ans = temp.solution(initTree)
    print(ans)