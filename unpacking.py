def urutan_email(domains):
    email = []
    for domain, users in domains.items():
        for user in users:
            email.append(user + "@" + domain)
    return email

print(urutan_email({"gmail.com": ["kenta", "edmonda", "andi"], "yahoo.com": ["samsul.bahri", "jeni.rosi"], "hotmail.com": ["kali.urang"]}))
