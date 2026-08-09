import hashlib

def crack_sha1_hash(hash, use_salts=False):
    # Cargar las contraseñas
    with open("top-10000-passwords.txt", "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f]

    # Cargar los salts si use_salts es True
    salts = []
    if use_salts:
        with open("known-salts.txt", "r", encoding="utf-8") as f:
            salts = [line.strip() for line in f]

    for pwd in passwords:
        if use_salts:
            for salt in salts:
                # Probar salt antes (prepend)
                test_str_pre = (salt + pwd).encode("utf-8")
                if hashlib.sha1(test_str_pre).hexdigest() == hash:
                    return pwd
                
                # Probar salt después (append)
                test_str_app = (pwd + salt).encode("utf-8")
                if hashlib.sha1(test_str_app).hexdigest() == hash:
                    return pwd
        else:
            # Sin salts
            test_str = pwd.encode("utf-8")
            if hashlib.sha1(test_str).hexdigest() == hash:
                return pwd

    return "PASSWORD NOT IN DATABASE"