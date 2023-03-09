


def checkmoney(money):
    for m in money.items():
        if m[1] >=400:
            print(m[0], m[1])

money = {'somjai':222,'somsri':1992,'somyod':50,'yodchai':400}
checkmoney(money)
money = {'somjai':222,'somsri':1992,'somyod':50,'yodchai':400,'siwat':800}
checkmoney(money)
