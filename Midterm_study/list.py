def numItems():
    if self.next == None:
        return
    self.__numItems += 1
    numItems()