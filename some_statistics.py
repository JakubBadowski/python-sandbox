#! python3


import statistics as st


ex_list = [3,6,3,6,7,7,5,4,3,3,5,3,6,7,2,5,2,8,4]

mean = st.mean(ex_list)         # średnia arytmenyczna
median = st.median(ex_list)     # mediana 
stdev = st.stdev(ex_list)       # odchylenie standardowe

print(mean, median, stdev)


