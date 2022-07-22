'''Write a Python function that takes two lists and returns true if they have
at least one common member'''
def common(l1,l2):
    for i in l1:
        if i in l2:
            print("true")
            break
    else:
        print("false")
l1=[1,5,"lk",96]
l2=["po",4,5]
common(l1,l2)