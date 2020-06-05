
class ColorManager(object):
    def __init__(self):
        self.gray = self.rgb_to_hex((50, 50, 50))
        self.dark_gray = self.rgb_to_hex((33, 33, 33))
        self.light_gray = self.rgb_to_hex((169, 169, 169))
        self.blue = self.rgb_to_hex((51, 94, 145))
        self.red = self.rgb_to_hex((107, 42, 28))
        self.green = self.rgb_to_hex((53, 112, 52))
        self.white = self.rgb_to_hex((255, 255, 255))
        self.dark_blue = self.rgb_to_hex((26, 51, 82))

    @staticmethod
    def rgb_to_hex(rgb):
        return "#%02x%02x%02x" % rgb