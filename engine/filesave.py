# In this file there is the logic for saving and loading the levels
import json
import os


def level_save(savepath, savename, commands_as_string):
    with open(os.path.join(savepath, savename), "w") as file:
        file.write(json.dumps(commands_as_string))
    file.close()


def level_load(loadpath, loadname):
    with open(os.path.join(loadpath, loadname), "r") as file:
        commands = file.readlines()
    file.close()
    for command in commands:
        print(command, "-")
        test = "print('test')"
        exec("print('hello world!')")
        exec(test)
        exec(command.strip())
        print("-")


if __name__ == "__main__":
    level_save("levels", "prova.json", "print('hello world!')")
    level_load("levels", "prova.json")
