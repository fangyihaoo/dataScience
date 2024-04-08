class PointN:
    def __init__(self, *args):
        if isinstance(args[0], list):
            self.the_list = [i for i in args[0]]
        else:
            self.the_list = [i for i in args]
        self.list_len = len(self.the_list)
    
    def __str__(self):
        all_list = [str(i) for i in self.the_list]
        return 'point(' +', '.join(all_list) + ')'

    def __add__(self,other):
        hy = zip(self.the_list, other.the_list)
        new_list = [x+y for x,y in hy]
        return PointN(new_list)

if __name__ == '__main__':
    p1 = PointN(1,2,3,4)
    p2 = PointN([4,5,6,7,8])
    print(f"sum: {p1+p2}") 