import numpy as np
 
def main():
    array_value = np.array([1,3,5,7,9,11])
    print("integer np array {} \n".format(array_value))

    array_string_value = np.array(["red", "green", "yellow"])
    print("string np array {} ".format( array_string_value) )
    print("data type {} ".format(array_string_value.dtype)) # datatype <U6 max length of "yellow"

    array_date_value = np.array(["1990-10-04", "1989-05-06", "1990-11-04"])
    print("string date value {}, dtype {}".format(array_date_value, array_date_value.dtype))

    my_datetime_array = array_date_value.astype("M")
    print("astype result : ", my_datetime_array.dtype)

    array_date_value_for_dtype = np.array(["1990-10-04", "1989-05-06", "1990-11-04"], dtype = "M")
    print("dtype setting {}, type {} ", array_date_value_for_dtype, array_date_value_for_dtype.dtype)

if __name__ == "__main__":
    main()