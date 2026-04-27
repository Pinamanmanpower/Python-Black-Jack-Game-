import time
def loading_animation(duration):
    print("loading", end="")
    for _ in range(duration):
        print(".", end="")
        time.sleep(0.5)


    print()

loading_animation(5)