def replace_domain(mail, new, old = "kaaj.com"):
    new_mail = mail.split("@")
    if new_mail[1] == old:
        print(new_mail[0]+"@"+new)
    else:
        print(mail)
replace_domain("alice@kaaj.com", "sheba.xyz", "kaaj.com")