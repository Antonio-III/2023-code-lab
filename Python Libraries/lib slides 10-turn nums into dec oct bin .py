class App():
    def __init__(self,minn,maxn):
        print('Numbering System Table')
        print(f'Decimal\tOctal\tHex\tBinary')
        
        for i in range(minn,maxn):
            print(f'{i}\t{oct(i)}\t{hex(i)}\t{bin(i)}')


if __name__=='__main__':
    App(0,101)
