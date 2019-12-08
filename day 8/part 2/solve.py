with open("input.txt", "r") as file:
    data = [int(val) for val in file.read().strip()]

SZ = (25, 6)


class Layer:
    def __init__(self, size, pixels):
        self.pixels = []
        self.raw_pixels = pixels
        for y in range(size[1]):
            row = []
            for x in range(size[0]):
                row.append(pixels[y * size[0] + x])
            self.pixels.append(row)

    def get_num_of(self, num):
        count = 0
        for px in self.raw_pixels:
            count += 1 if px == num else 0
        return count


class Image:
    def __init__(self, size, pixels):
        self.layers = []
        self.size = size
        res = size[0] * size[1]
        for l in range(len(pixels) // res):
            self.layers.append(Layer(size, pixels[ (l * res):((l+1) * res) ]))

    def solve(self):
        least_zeros = (self.layers[0].get_num_of(0), self.layers[0])
        for l in self.layers[1:]:
            num_zeros = l.get_num_of(0)
            least_zeros = (num_zeros, l) if num_zeros < least_zeros[0] else least_zeros
        return least_zeros[1].get_num_of(1) * least_zeros[1].get_num_of(2)

    def display(self):
        to_show = [2] * (self.size[0] * self.size[1])
        for l in self.layers:
            for px_num, px in enumerate(l.raw_pixels):
                if to_show[px_num] == 2:
                    to_show[px_num] = px
        chars = ["▓", "▒", " "]
        to_show_str = "".join(map(lambda px: chars[px], to_show))
        
        for row in range(self.size[1]):
            print(to_show_str[ (row * self.size[0]):((row+1) * self.size[0]) ])
        



img = Image(SZ, data)
img.display()