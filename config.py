import configparser

# Создаём объект для парсинга INI-файлов
config = configparser.ConfigParser()
config.read('config.ini')

# Из config достаем нужные значения
ip = config["IP"]["ip"]
login = config["AUTH"]["login"]
password = config["AUTH"]["password"]
ldap_name = config["LDAP"]["ldap_name"]
ldap_bind_uri = config["LDAP"]["ldap_bind_uri"]
ldap_bind_user = config["LDAP"]["ldap_bind_user"]
ldap_password = config["LDAP"]["ldap_password"]
ldap_base_dn = config["LDAP"]["ldap_base_dn"]
