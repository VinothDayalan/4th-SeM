# from multiprocessing import Process
# from cryptography.fernet import Fernet
# import time 
# def f(value):
#     key = Fernet.generate_key()
#     fernet = Fernet(key)
#     encMessage = fernet.encrypt(value.encode())
#     print("encrypted string: ", encMessage)
# if __name__ == '__main__':
#     _value=input()
#     for i in 
#     p = Process(target=f, args=(_value,))
#     start = time.time()
#     p.start()
#     a = 0
#     for i in range(1000):       
#         a += (i**100)
#     p.join()
#     end = time.time()
#     print("The time of execution of above program is :",(end-start) * 10**3, "ms")



# from multiprocessing import Pool
# from cryptography.fernet import Fernet
# import string
# import random
# import time
# def f(value):
#     key = Fernet.generate_key()
#     fernet = Fernet(key)
#     encMessage = fernet.encrypt(value.encode())
#     return encMessage
# if __name__ == '__main__':
#     start = time.time()
#     a = 0
#     for i in range(1000):       
#                 a += (i**100)
#     with Pool(5) as p:
        
#         for i in range(1,1001):
#             _ascii=chr (i)
#             print(p.map(f, [_ascii]))
            
#     end = time.time()
#     print("The time of execution of above program is :",(end-start) * 10**3, "ms")

# from cryptography.fernet import Fernet
# import time
# def f(value):
#     key = Fernet.generate_key()
#     fernet = Fernet(key)
#     encMessage = fernet.encrypt(value.encode())
#     return encMessage
# if __name__ == '__main__':
#     start = time.time()
#     a = 0
#     for i in range(1,1001):
#         _ascii=chr (i)
#         print(f(_ascii))
#         # for i in range(1000):       
#         #     a += (i**100)
#     end = time.time()
#     print("The time of execution of above program is :",(end-start) * 10**3, "ms")


# from cryptography.fernet import Fernet
# import time
# def f(value):
#     return value**value
# if __name__ == '__main__':
#     start = time.time()
#     a = 0
#     for i in range(1,101):
#         print(f(i))
#         # for i in range(1000):       
#         #     a += (i**100)
#     end = time.time()
#     print("The time of execution of above program is :",(end-start) * 10**3, "ms")



# from multiprocessing import Pool
# import time
# def f(value):
#     return value**value
# if __name__ == '__main__':
#     start = time.time()
#     with Pool(1) as p:
#         for i in range(1,101):
#             print(p.map(f, [i]))
            
#     end = time.time()
#     print("The time of execution of above program is :",(end-start) * 10**3, "ms")

import time
from multiprocessing import Pool
def f(x):
    return x*x
if __name__ == '__main__':
    start = time.time()
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
    end = time.time()
    print("The time of execution of above program is :",(end-start) * 10**3, "ms")



import time
def f(value):
    return value**value
if __name__ == '__main__':
    start = time.time()
    for i in range(1,4):
        print(f(i))
    end = time.time()
    print("The time of execution of above program is :",(end-start) * 10**3, "ms")