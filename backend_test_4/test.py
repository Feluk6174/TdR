from netifaces import interfaces, ifaddresses, AF_INET

for iface_name in interfaces():
    print(iface_name)
    adddress = [i['addr'] for i in ifaddresses(iface_name).setdefault(AF_INET,[{'addr':'no IP addr'}])]
    print(' '.join(adddress))