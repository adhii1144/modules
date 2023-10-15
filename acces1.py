from data1 import list1
import data1.string1 as st
import data1.tuple1 as tu
import data1.dictionary1 as dt
l = list1.lsti()
x = map(lambda x : x * 2,l)
print('doubled elements are : {}'.format(list(x)))
y = st.srting()
print("String :{}".format(y))
z = tu.tple()
print("Tuple :{}".format(tuple(z)))
e = dt.dit()
print("Dictionary is :{}".format(e))