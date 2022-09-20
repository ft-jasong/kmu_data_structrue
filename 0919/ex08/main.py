from element import Element

size = 10
list_ = [0] * size
print(list_)

# list_ = [Element(10)] * size # 같은 reference를 계속 참조함.
list_ = [Element(10) for _ in range(10)] # 
print(list_)

list_[0].value = 99
print(list_)

