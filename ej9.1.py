def validar_email(email):
    if "@" not in email or "." not in email:
        return False
    nombre, dominio = email.split("@")
    if len(dominio.split(".")) < 2:
        return False
    return True
