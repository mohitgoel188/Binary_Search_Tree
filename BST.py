class Node:
    def __init__(self,data):
        self.left=self.right=None
        self.data=data

class BST:

    def insert(self,data,root):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                new=self.insert(data,root.left)
                root.left=new
            if data>root.data:
                new=self.insert(data,root.right)
                root.right=new
        return root

    def depth(self,root):
        if root.left==None and root.right==None:
            return 1
        else:
            l=r=0
            if root.left!=None:
                l=1+self.depth(root.left)
            if root.right!=None:
                r=1+self.depth(root.right)
            return max(l,r)

    def bfs(self,root):             #Breath First Search
        queue=[root]
        while len(queue)!=0:
            r=queue.pop(0)
            print(r.data,end=' ')
            if r.left!=None:
                queue.append(r.left)
            if r.right!=None:
                queue.append(r.right)

    def dfs(self,root):             #Depth First Search
        print(root.data,end=' ')
        if root.left!=None:
            self.dfs(root.left)
        if root.right!=None:
            self.dfs(root.right)


def main():
    tree=BST()
    print('Enter total number of nodes in tree:')
    L=int(input())
    print('Enter values of Node:')
    root=None
    for i in range(L):
        data=int(input())
        root=tree.insert(data,root)
    print(f'\nDepth Of Tree {tree.depth(root)}\nBFS: ',end='')
    tree.dfs(root)

if __name__ == '__main__':
    main()
