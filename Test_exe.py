number_value = "a,0,x"
IsFormat= number_value.split(',')
if(len(IsFormat)==3):
    print(isinstance(int(IsFormat[0]),int))
    if isinstance(int(IsFormat[0]),int) and isinstance(int(IsFormat[1]),int):
        print("格式正确")
    else:
        print("格式不正确")
else:
    print("格式x不正确")