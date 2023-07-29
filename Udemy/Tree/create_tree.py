class TreeNode:
    
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
        
    def __str__(self, level=0):
        ret = " "*level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode("Cold", [])
hot = TreeNode("hot", [])

tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode("tea", [])
cofee = TreeNode("cofee", [])
hot.addChild(tea)
hot.addChild(cofee)

cola = TreeNode("cola", [])
pepsi = TreeNode("pepsi ", [])

cold.addChild(cola)
cold.addChild(pepsi)
print(tree)