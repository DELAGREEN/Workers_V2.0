#coding=1251
# Configurator
s = '*'*3
p = ' '*10
# end

#�����������
def privet():
    print(p+'*'*50)
    print(p+s+"����������� � ���������: ��������� ������!!"+s)
    print(p+"��� ��� ������?? (������� ������� ����� � ������� Enter)")
    print(p+"1 - �������� ������ ����������")
    print(p+"2 - ������� ����������")
    print(p+"3 - ���������� ������ �����������")
    return privet

#************************************************************
#************************************************************
#************     ������� ----- DATA              ***********
#************************************************************
#************************************************************
data = []
pre_data = []
#************************************************************
#************************************************************
#************************************************************
#************************************************************

#���������� ����������
def vjob():

    pre_data = str(input(p+"������� ��� ����������: "))
    data.append(pre_data)

    pre_addres = str(input(p+"������� ����� ����� ���������� ����������: "))
    addres.append(pre_addres)

    return vjob


#����� ���� ��������� �� ������ �����������
def how_many_workers():
    print("�����"+p+"��� ���������"+p+"����� ����������")
    data_len = len(data)
    addres_len = len(addres)
    i=0
    j=0
    while i < data_len and addres_len:
        print(p+"-" * 50)
        print(i+1,p,data[i], p,addres[j])
        i+=1
        j+=1

def data_off_size():
    a = len(data)
    if a <= 0:
        print(p+p+"��������")
        print(p+"������ ����������� ����!!!")
        print(p+"��� ������ ������ � �����, ��������� ������ �����������")
        menu()
    else:
        how_many_workers()


def menu():
    while True:

        privet()

        console_input = int(input(p+"������� ����� �������: "))

        if console_input == 1:
            vjob()
            print(p+"�������� ������� �� ������")
        
        elif console_input == 2:
            print(p+"1 - ������� ���� ������ ������� ���������� �� ������ � ������")
            print(p+"2 - ������� ���� ��������� ���� ���")
            console_input2 = int(input(p+"������� ����� �������: "))
        
            if console_input2 == 1:
                data_off_size()
                how_many_workers()
                i = int(input("������� ���������� �������� ������� ��� ���������� ���������: "))
                b = i - 1
                del data[b]
                del addres[b]
                print("�������� ������.")


            elif console_input2 == 2:
                data_off_size()
                how_many_workers()
                index = data.index(str(input("������� ���� ���� ������ �������: ")))
                del data[index]
                del addres[index]
                print(p+"��������� ��� ������.")
            else:
                print(p+"������, ������� �� ����������.")
     

        elif console_input == 3:
            a = len(data)
            if a <= 0:
                print(p+p+"��������")
                print(p+"������ ����������� ����!!!")
                print(p+"��� ������ ������ � �����, ��������� ������ �����������")
        

            else:
                how_many_workers()
        


        else:
            print(p+"������, ������� �� �����������.")
menu()