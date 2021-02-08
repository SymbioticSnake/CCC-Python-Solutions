class PathSet:
    def __init__(self):
        self.paths = [None]*2
        self.numItems = 0
        self.history = []

    def __len__(self):
        return self.numItems

    def __extend(paths):
        newSet = [None] * 2 * len(paths)
        for item in paths:
            PathSet.__add(item, newSet)

        return newSet

    def add(self, path):
        if PathSet.__add(path, self.paths):
            self.numItems += 1
            capacity = self.numItems / len(self.paths)

            if capacity >= 0.75:
                self.paths = PathSet.__extend(self.paths)

    def __add(path, paths):
        for i in range(len(paths)):
            if paths[i] == path:
                return False

            if paths[i] == None:
                paths[i] = path
                return True

    def __iter__(self):
        for item in self.paths:
            if item != None:
                yield item

    def __contains__(self, item):
        return item in self.paths

    def addToHis(self, path):
        self.history.append(path)

def main():
    p = PathSet()
    p.add(1)
    p.add(2)

if __name__ == "__main__": main()