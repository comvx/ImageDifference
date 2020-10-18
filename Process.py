import tqdm

class defPoints:
    def __init__(self, data):
        self.data = data
        self.compData = None

    def proc(self):
        data = self.data
        bar = tqdm.tqdm(total=len(data))
        for index in range(len(data)):
            if(index == 0):
                self.compData = data[index]
                next
            else:
                frame = data[index]#current
                #print(str(frame_2.get_diff()) + "//" + str(frame_1.get_diff()))
                if(frame.get_diff() > 6.0):
                     frame.set_point(True)
                data[index] = frame
            bar.update(1)
        return data