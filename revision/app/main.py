import logging

from oop.models import Person, Bank
from revision import utils
from logger import logger


def main():
    utils.is_number_bigger_than_threshold(5, 8)
    utils.is_number_bigger_than_threshold(15, 8)
    utils.is_number_bigger_than_threshold(30, )
    utils.is_number_bigger_than_threshold(5, )

    logger.info('Hello here!!!')
    # logger.warning('Hello warning!!!', extra={"user": 123})
    # logger.error('Hello warning!!!', extra={"user": 123})
    logger.debug('Hello warning!!!', extra={"user": 5555})
    # logger.fatal('Hello warning!!!', extra={"user": 123})

    # print(True + 1 + 2.5)
    vasil = Person(name='Vasil')
    print(vasil.__dict__)
    alex = Person("alex")
    marta = Person("Marta")
    john = Person("john")

    mono = Bank('mono')
    raif = Bank('raif')

    raif_acc_john = raif.open_account(john)
    raif_acc_alex = raif.open_account(alex)
    raif_acc_marta = raif.open_account(marta)
    raif.open_account(marta)
    mono_acc_marta = mono.open_account(marta)

    mono_acc_marta.transfer(500, raif_acc_alex)
    mono_acc_marta.deposit(5225)
    mono_acc_marta.deposit(5225)
    raif_acc_marta.deposit(5225)
    mono_acc_marta.deposit(5225)
    print(8888888888, raif.accounts[0].owner.name)
    raif_acc_john.withdraw(15000)
    print(raif.__dict__)
    print(mono.__dict__)
    print(marta.__dict__)
    print(mono)
    print([mono, raif])
    print(raif.total_money)
    print(marta.total_money)


if __name__ == "__main__":
    main()
