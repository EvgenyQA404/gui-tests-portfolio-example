import config


class Data:
    # Главная страница
    main_page = f"http://{config.ip}:8000/ngate-web-console/login"
    # Ldap страница
    ldap_page = f"http://{config.ip}:8000/ngate-web-console/ldap-server"
    ldap_name = config.ldap_name
    ldap_bind_uri = config.ldap_bind_uri
    ldap_bind_user = config.ldap_bind_user
    ldap_password = config.ldap_password
    ldap_base_dn = config.ldap_base_dn

    # Тестовые данные для ввода
    user_login = config.login
    user_password = config.password
    bad_login = "bad"
    bad_password = "bad"

    # Ожидаемые результаты
    text_panel_ngate = "nGate Control Panel"
    dashboard = "Welcome, ng-admin!"
    error_login = "Login or password is incorrect"
    error_sign_out_profile = "NGate Web Console"

    # ldap
    # Сообщение об успешном создании LDAP
    access_created_ldap = "LDAP Server created"
    # Сообщение об успешном копировании LDAP
    access_copy_ldap = "Object copied"
    # Сообщение об успешном копировании LDAP
    access_deleted_ldap = '"LDAP" deleted.'
    # Сообщение об ошибке при дубликате LDAP
    error_duplicate_ldap = "Field LDAP Name should not be repeated between objects. Please choose another value."
    # Описание LDAP
    ldap_description = "This is LDAP"
    # Имя копии LDAP
    name_copy_ldap = "LDAP [copy]"
