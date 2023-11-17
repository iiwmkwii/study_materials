def main():
    x, y = 100, 100
    width, height = 200, 200
    draw_house(x, y, width, height)


def draw_house_foundation(x, y, width, height):
    pass


def draw_house_walls(x, y, width, height):
    pass


def draw_house_roof(x, y, width, height):
    pass



def draw_house(x, y, width, height):
    """
    Рисовать домик ширины width и высоты height от опорной точки (x, y),
    которая находится в середине нижней точки фундаментаю
    :param x: координата x середины домика
    :param y: координата y низа фундамента
    :param width: полная ширина домика (фундамент или вылеты крышы включены)
    :param height: полная высота домика
    :return: none
    """
    print('Активное строительство дома...', x, y, width, height)
    foundation_height = 0.05 * height
    walls_height = 0.5 * height
    walls_width = 0.9 * width
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)

main()