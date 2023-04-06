acl_num = input("Introduce el número de ACL IPv4: ")

if acl_num.isdigit():
    acl_num = int(acl_num)
    if acl_num >= 1 and acl_num <= 99:
        print("ACL Estándar")
    elif acl_num >= 100 and acl_num <= 199:
        print("ACL Extendida")
    else:
        print("El número no corresponde a una lista de acceso")
else:
    print("Por favor, introduce un número entero válido")
