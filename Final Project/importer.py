from settings import *

def audio_loader(*path):
    audio_dict = {}
    for dirpath, _, filenames in walk(join(*path)):
        for file in filenames:
            if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.ogg'): 
                pygame.mixer.init()
                audio_dict[file.split('.')[0]] = pygame.mixer.Sound(join(dirpath, file))
            else: print(f"Unsupported audio format: {file}")
    return audio_dict

def import_images(*path):
    images = {}
    for dirpath, _, filenames in walk(join(*path)):
        for file in filenames:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                try: images[file.split('.')[0]] = pygame.image.load(join(dirpath, file)).convert_alpha()
                except pygame.error as e: print(f"Error loading image {file}: {e}")
            else:
                print(f"Unsupported image format: {file}")
                print(f"Full path: {join(dirpath, file)}")
    return images