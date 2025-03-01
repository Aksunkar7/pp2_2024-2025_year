def to_boolean(value):
    if value.lower() == "true":  #Адамдар әртүрлі жазып  тастауы мүмкін сол үшін кішірейтеміз
        return True
    elif value.lower() == "false":
        return False
    else:
        return bool(int(value)) #элемент стринг болып тұрады егер ол 0,1 болса инт айналдырып тексереміз

tup = tuple(map(to_boolean, input("booleans: ").split())) #Біз енгізген әр элемент мап арқасында функцияға кіріп шығады,
                                                          #элемент булеан болса кайтарады

print(all(tup)) #Ішіндегі барлық элем True болса True қайтарады
