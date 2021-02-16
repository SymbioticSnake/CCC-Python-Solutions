# class EscapeRoom:
#     class ER_Node:
#         class PathList:
#             def __init__(self):
#                 self.paths = [None]*2
#                 self.numItems = 0
#                 self.history = []

#             def __len__(self):
#                 return self.numItems

#             def __extend(paths):
#                 newSet = [None] * 2 * len(paths)
#                 for item in paths:
#                     EscapeRoom.ER_Node.PathList.__append(item, newSet)

#                 return newSet

#             def append(self, path):
#                 if EscapeRoom.ER_Node.PathList.__append(path, self.paths):
#                     self.numItems += 1
#                     capacity = self.numItems / len(self.paths)

#                     if capacity >= 0.75:
#                         self.paths = EscapeRoom.ER_Node.PathList.__extend(self.paths)

#             def __append(path, paths):
#                 for i in range(len(paths)):
#                     if paths[i] == path:
#                         return False

#                     if paths[i] == None:
#                         paths[i] = path
#                         return True

#             def __iter__(self):
#                 for item in self.paths:
#                     if item != None:
#                         yield item

#             def __contains__(self, item):
#                 return item in self.paths

#             def addToHis(self, path):
#                 self.history.append(path)

#         def __init__(self, val, coor):
#             self.val = val
#             self.coor = coor
#             self.paths = EscapeRoom.ER_Node.PathList()

#         def getVal(self):
#             return self.val

#         def setVal(self, newval):
#             self.val = newval

#         def getCoor(self):
#             return self.coor

#         def addPath(self, path):
#             self.paths.append(path)

#         def __iter__(self):
#             yield (self.val, self.coor)

#             if len(self.paths) != 0:
#                 for elem in self.paths:
#                     yield elem

#         def __repr__(self):
#             return "ER_Node(" + repr(self.val) + ", " + repr(self.coor) + ")"

#     def __init__(self, matrix):
#         self.root = matrix[0][0]
    
#     def insert(self, val, coor):
#         self.root = EscapeRoom.__insert(self.root, val, coor)
    
#     def __insert(root, val, coor):
#         if root == None and coor[0]*coor[1] == root.getVal():
#             return EscapeRoom.ER_Node(val, coor)
        
#         for path in root.paths:
#             self.


def factor_coordinates(dividend, num_rows, num_columns):
    c_list = []

    d = int(dividend)
    r = int(num_rows)
    c = int(num_columns)

    for i in range(1, int(d)+1):
        if d % i == 0:
            c_list.append((i, d // i))

    c_list = [co for co in c_list if co[0] <= r]
    c_list = [co for co in c_list if co[1] <= c]

    return c_list


def main():
    table = []
    num_rows = int(input())
    num_columns = int(input())

    for _ in range(num_rows):
        row = input().split()
        table.append(row)

    for row in table:
        for i in range(4):
            row[i] = int(row[i])

    # print(table)

    # history = []

    # coor = (1, 1)
    # start = ER_Node(table[ coor[0]-1 ][ coor[1]-1 ], coor)
    # history.append(start)

    # factors = factor_coordinates(start.getVal(), num_rows, num_columns)
    # history[0]
    

if __name__ == "__main__":
    main()
