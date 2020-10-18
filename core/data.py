class imageData:
    def __init__(rgb, wb, diff, index):
        self.rgb = rgb
        self.wb = wb
        self.diff = diff
        self.point = False
        self.index = index

    def set_point(self, status):
        self.status = status
    def get_point(self):
        return self.status

    def get_rgb(self):
        return self.rgb
    def get_wb(self):
        return self.wb
    def get_diff(self):
        return self.diff
    def get_index(self):
        return self.index