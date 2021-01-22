while (true) {
    if (input.lightLevel() < 6 && input.soundLevel() >= 150) {
    } else {
        light.setAll(light.rgb(255, 0, 0))
    }
    
}
