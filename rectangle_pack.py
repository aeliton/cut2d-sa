class RetanglePack:

    def __init__(self, height, width):
        self.binWidth = width;
        self.binHeight = height;
        self.root.left = self.root.right = 0;
        self.root.x = self.root.y = 0;
        self.root.width = width;
        self.root.height = height;

    def Occupancy(self):
        self.totalSurface = self.binHeight * self.binWidth
        self.usedSurface = self.UsedSurface(self.root)
        return self.usedSurface / self.totalSurface

    def UsedSurface(self, node):
        if node.left or node.right:
            usedSurface = node.width * node.height
            if node.left:
                usedSurface += self.UsedSurface(node.left)
            if node.right:
                usedSurface += self.UsedSurface(node.right)
            return usedSurface

        return 0

    def Insert(self, node, width, height):
        w = node.width - width
        h = node.height - height


        if w <= h:
            node.left.x = node.x + width
            node.left.y = node.y
            node.left.width = w
            node.left.height = height

            node.right.x = node.x
            node.right.y = node.y + height
            node.right.width = node.width
            node.right.height = h
        else:
            node.left.x = node.x
            node.left.y = node.y + height
            node.left.width = width
            node.left.height = h

            node.right.x = node.x + width
            node.right.y = node.y
            node.right.width = w
            node.right.height = height

        node.width = width
        node.height = height

        return node

