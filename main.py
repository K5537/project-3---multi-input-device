while True:
    if input.light_level() < 6 and input.sound_level() >= 150:
        def on_forever():
            pass
            forever(on_forever)
            music.magic_wand.loop()
            pause(1000)
            music.magic_wand.loop()
            pause(200)
    else:
        light.set_all(light.rgb(255, 0, 0))