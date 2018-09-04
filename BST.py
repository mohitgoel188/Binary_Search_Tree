class Node:
    def __init__(self,datum):
        self.left=self.right=None
        self.next=None      # if connecting levels
        self.datum=datum

class BST:
    def insert(self,datum,root):
        if root==None:
            return Node(datum)
        else:
            if datum<=root.datum:
                new=self.insert(datum,root.left)
                root.left=new
            if datum>root.datum:
                new=self.insert(datum,root.right)
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

    def find_diameter(self,root):
        lmax=rmax=0
        if root.left!=None:
            lmax=1+self.depth(root.left)
        if root.right!=None:
            rmax=1+self.depth(root.right)
        return lmax+rmax 

    def connect_level_nodes(self,root,first_node=None,pre_node=None):
        if root.left!=None:
            if first_node==None:
                first_node=root.left
            if pre_node!=None:
                pre_node.next=root.left
            pre_node=root.left
            if root.right!=None:
                root.left.next=root.right
                pre_node=root.right
        elif root.right!=None:
            if first_node==None:
                first_node=root.right
            if pre_node!=None:
                pre_node.next=root.right
            pre_node=root.right    
        if root.next!=None:
            self.connect_level_nodes(root.next,first_node,pre_node)
        elif first_node!=None:
            self.connect_level_nodes(first_node)

    def bfs(self,root,mode='parse',searchitem=None):             #Breath First Search
        queue=[root]
        while len(queue)!=0:
            r=queue.pop(0)
            if mode=='search':
                if r.datum==searchitem:
                    return r
            else:
                print(r.datum,end=' ')
            if r.left!=None:
                queue.append(r.left)
            if r.right!=None:
                queue.append(r.right)

    def dfs(self,root):             #Depth First Search
        print(root.datum,end=' ')
        if root.left!=None:
            self.dfs(root.left)
        if root.right!=None:
            self.dfs(root.right)

    def sts(self,left_helix=True,root=None,mode='parse',searchItem=None):   #Spiral Traversal/Search
        if left_helix:
            if root!=None:
                self.lh=[root]
                self.rh=[]
            while len(self.lh)>0:
                exNode=self.lh.pop()
                if mode=='parse':
                    print(exNode.datum,end=' ')
                else:
                    if exNode.datum==searchItem:
                        return exNode
                if exNode.right!=None:
                    self.rh.append(exNode.right)
                if exNode.left!=None:
                    self.rh.append(exNode.left)
            if len(self.rh)>0:
                self.sts(False)
        else:
            if root!=None:
                self.lh=[]
                self.rh=[root]
            while len(self.rh)>0:
                exNode=self.rh.pop()
                if mode=='parse':
                    print(exNode.datum,end=' ')
                else:
                    if exNode.datum==searchItem:
                        return exNode
                if exNode.left!=None:
                    self.lh.append(exNode.left)
                if exNode.right!=None:
                    self.lh.append(exNode.right)
            if len(self.lh)>0:
                self.sts(True)

    def delete(self,root,item):
        node=self.bfs(root,mode='search',searchitem=item)
        if node.left==None:
            node.datum=0
        while node.left.left != None:
            node.datum=node.left.datum
        node.datum=node.left.datum
        node.left=None

def main():
    tree=BST()
    print('Enter total number of nodes in tree:')
    L=int(input())
    print('Enter values of Node:')
    root=None
    for i in range(L):
        datum=float(input())
        root=tree.insert(datum,root)
    while True:
        choice=int(input('\n\n\tBST Operations Menu:-\n1. Insert\n2. Delete\n3. Traverse\n4. Depth\n5. Diameter\n6. Connect Level Nodes\n7. Exit\n\nEnter your choice: '))
        if choice==1:
            datum=input('Enter Value: ')
            root=tree.insert(float(datum),root)
        elif choice==2:
            datum=input('Enter value of node to be deleted: ')
        elif choice==3:
            way=int(input('\nHow does the parsing happen:\n1. Breadth First\n2. Depth First\n3. Spiral\n\nEnter your choice: '))
            if way==1:
                print('BFS: ',end='')
                tree.bfs(root)
            elif way==2:
                print('DFS: ',end='')
                tree.dfs(root)
            elif way==3:
                helical=input('Helix-> Left first(l)\\Right first(r): ')
                if helical.lower()=='r':
                    left_helix=False
                else:
                    left_helix=True
                print('\nSpiral: ',end='')
                tree.sts(left_helix,root)
        elif choice==4:
            print(f'\nDepth Of Tree: {tree.depth(root)}')
        elif choice==5:
            print(f"\nDiameter of Tree: {tree.find_diameter(root)}")
        elif choice==6:
            tree.connect_level_nodes(root)
            node=root
            while node!=None:
                first_node=node.left
                while first_node!=None:
                    print(first_node.datum)
                    first_node=first_node.next
                node=node.left
        elif choice==7:
            break    

if __name__ == '__main__':
    main()
