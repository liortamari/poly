class MagicList(list):

    def __init__(self, cls_type=object):
        super(MagicList, self).__init__()
        self.cls_type = cls_type

    def __getitem__(self, key):
        if key == self.__len__() and self.cls_type != object:
            item = self.cls_type()
            self.append(item)
        return super(MagicList, self).__getitem__(key)

    def __setitem__(self, key, value):
        if key == self.__len__():
            return self.append(value)
        else:
            return super(MagicList, self).__setitem__(key, value)