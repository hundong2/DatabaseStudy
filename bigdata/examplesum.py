import numpy as np

def main():
   arr = np.arange(0, 4*2*4)
   print("array \n{}\n".format(arr))
   v = arr.reshape([4,2,4])
   print("array reshape\n{}\n".format(v))

   print("ndim(dimension) {}, summary {}\n".format(v.ndim, v.sum()))
   print("sum axis =0 \n{}\n{}\n".format(v.sum(axis=0)))
   print("sum axis =1 \n{}\n".format(v.sum(axis=1)))

   '''
   ndim(dimension) 3, summary 496
   sum axis =0 
   [[48 52 56 60]
   [64 68 72 76]]
   sum axis =1 
   [[ 4  6  8 10]
   [20 22 24 26]
   [36 38 40 42]
   [52 54 56 58]]
   '''
if __name__ == "__main__":
   main()


