OSi = '''
    МОДЕЛЬ OSI
- Физический уровень (physical)
Работа со средой передачи, сигналами и двоичными данными

- Канальный уровень (data link): Ethernet
Физическая адресация

- Сетевой уровень (network): IPv4, IPv6
Определение маршрута и логическая адресация

- Транспортный уровень (transport): TCP, UDP, PORTS
Прямая связь между конечными пунктами и надёжность

- Сеансовый уровень (session)
Управление сеансом связи

- Представительский уровень (presentation)
Представление и шифрование данных

- Прикладной уровень (application): HTTP, FTP, POP3, WebSocket
Доступ к сетевым службам

- Viki_OSi_model (href)
https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%82%D0%B5%D0%B2%D0%B0%D1%8F_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_OSI
'''


def main():
    print(OSi)


if __name__ == '__main__':
    main()
