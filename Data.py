class genData():
    ori_size = (0,0)
class imageData:
    def __init__(self, rgb, wb, diff, index):
        #rgb[0] = r | rgb[1] = g | rgb[2] = b | rgb[3] = difference between passed + current
        #wb[0] = r | wb[1] = g | wb[2] = b | wb[3] = difference between passed + current
        #diff = difference between passed img + current
        #index = current index of file
        #point = point==True -> difference detected
        self.rgb = rgb
        self.wb = wb
        self.diff = diff
        self.point = False
        self.index = index

    def set_point(self, status):
        self.point = status
    def get_point(self):
        return self.point

    def get_rgb(self):
        return self.rgb
    def get_wb(self):
        return self.wb
    def get_diff(self):
        return self.diff
    def get_index(self):
        return self.index