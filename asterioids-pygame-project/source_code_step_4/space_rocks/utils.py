from pygame.image import load


def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)

    return loaded_sprite.convert_alpha() if with_alpha else loaded_sprite.convert()
