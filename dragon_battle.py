class Dragon:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def final_cry(self):
        print(self.name, 'is dead...')

    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def talk(self):
        print(self.name, self.health, '. Hit me!')


def main():
    enemy = Dragon('Smaug')
    enemy_list = [Dragon('Smaug'), Dragon('Hydra')]
    finish = False
    while not finish:
        enemy = enemy_list[0]
        enemy.talk()
        damage = int(input())
        enemy.get_damage(damage)
        if not enemy.is_alive(): # удалить из списка мёртвого врага
            enemy.final_cry()
            enemy_list.pop(0)
        if not enemy_list: # пуст ли список врагов
            finish = True
    print('You win!')










def dragon_talk():
    print('My health', health, '. Hit me!')


main()
