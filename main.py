# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    aux=aux2=0
    num=int(input("introduce un numbre"))
    while num < 1:
     num = int(input("introduce un numbre"))

    for x in range(num):
        aux+=1
        if aux < num:
            print(x,end="")
            aux2+=1
            print("la suma de les valor es ", aux2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

