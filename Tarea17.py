
def multi(list):

    multip = 0

    if len(list) > 0:

        multip = list[0]

        for i in range(1, len(list)):

            multip = multip * list[i]

        return multip

    else:

        print("Este arreglo no permite ser vacío!")


def main():

    list = [1,2,3,4]

    print(multi(list))


if __name__ == '__main__':

    main()