import matplotlib.pyplot as plt
x = [4,0]
y = [0,3]
%matplotlib inline
plt.plot(x,y)
x = [0,4,10]
y = [0,3,3]
plt.xlim(-10,25)
ply.ylim(-20,25)
%matplotlib inline
plt.plot(x,y)
def my_draw_a_vector_from_origin(v):
    #from origin to v
    plt.xlim(-10,15)
    plt.ylim(-10,15)
    x = [0,v[0]]
    y = [0,v[1]]
    plt.plot(x,v)
def my_draw_a_vector_from_v_to_w(v,w):
    #from origin to v
    x = [v[0],w[0]]
    y = [v[1],w[1]]
    plt.xlim(-10,55)
    plt.ylim(-2,55)
    plt.plot(x,y)
my_draw_a_vector_from_v_to_w([5,6],[20,16])
def my_scalar_product(a,b):
    return (a[0]*b[0]+a[1]*b[1])
v = [3,4]
w = [4,7]
my_scalar_product(v,w)
v = [0,4]
w = [3,0]

my_scalar_product(v,w)
my_draw_a_vector_from_origin(v)
my_draw_a_vector_from_v_to_w([5,5],[10,12])
my_draw_a_vector_from_origin([-7,5])
#my_draw_a_vector_from_origin([-7,5])
def distance(v,w):
    ((v[0]-w[0])**2)+((v[1]-w[1])**2)**.5
def my_vector_add(v,w):
    return [v[0]+w[0],v[1]+w[1]]
def my_vector_substract(v,w):
    return [v[0]-w[0],v[1]-w[1]]
def my_vector_multiply_with_scalar(c,v):
    return [c*v[0],c*v[1]]
a = [3,0]
b = [0,4]
print("toplam     : ",my_vector_add(a,b))
print("fark       : ",my_vector_substract(a,b))
print("5 katı (b) : ",my_vector_multiply_with_scalar(a,b))
print("uzunluk    : ",distance(a,b))
