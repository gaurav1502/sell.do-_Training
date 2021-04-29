
def frequency(a):
    aa=a.lower()
    count_b=aa.count("b")
    print("b",count_b)
    count_f=aa.count("f")
    print("f",count_f)
    count_j=aa.count("j")
    print("j",count_j)
    count_p=aa.count("p")
    print("p",count_p)
    count_v=aa.count("v")
    print("v",count_v)
    return count_b+count_f+count_j+count_p+count_v
print("Total",frequency("rajasoftwarelabs"))    