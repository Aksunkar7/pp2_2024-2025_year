import datetime
def drop_microseconds(date): #Микросекундты удалить ететін функция
    return date.replace(microsecond=0)

date = datetime.datetime.now() #today- дан айырмашылығы timezone шақыра алады, уақыт белдеуіне доступ береді (қажет болса)
print(drop_microseconds(date)) 

    