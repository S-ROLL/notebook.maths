def phepnhan(a,b):
    c = a * b
    return c

def tong_2_phepnhan(a,b):
    c = a + b
    print('Tong 2 phep nhan la',c)

a = int(input('Nhap vao a: '))
b = int(input('Nhap vao b: '))
c = int(input('Nhap vao c: '))
d = int(input('Nhap vao d: '))
tong_2_phepnhan(phepnhan(a,b),phepnhan(c,d))