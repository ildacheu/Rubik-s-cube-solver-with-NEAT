import cube2

u = cube2.player()
configcube = None

while True:
    try:
        configcube = u.play(configcubecube = configcube)
        cube2.show(configcube)
    except KeyboardInterrupt:
        break
