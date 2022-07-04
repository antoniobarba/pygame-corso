# In this file there is the logic for saving and loading the levels
import json
import os


class Save:
    @staticmethod
    def level_save(savepath: str, savename: str, scenes: list):
        """Scene must be a list containing all the scenes that must be saved."""
        json_to_save = []
        for scene in scenes:
            to_save_dict = scene.__dict__
            print(to_save_dict)
            for item in to_save_dict:
                if type(item) == "__main__":
                    print("CLASSE!!")
                else:
                    json_to_save.append(
                        (item, value) for item, value in scene.__dict__[item]
                    )
            # json_to_save.append(json.dumps(scene.__dict__))
        with open(os.path.join(savepath, savename), "w") as file:
            file.write(json.dumps(json_to_save))
        file.close()

    @staticmethod
    def _recursive_class_reading(cls):
        pass

    @staticmethod
    def _get_attributes(cls):
        results = []
        for attribute, value in cls.__dict__.items():
            results.append((attribute, value))
        return results

    @staticmethod
    def _class_to_dict(cls):
        result_dict = {}
        attributes = Save._get_attributes(cls)
        for key, value in attributes:
            print(key, value)
            # if "__main__." in str(type(value)) #this is for testing if value is a class, but need to be adjusted

            # I'll brute force it for now, but we need a way to keep the code more mantenaible
            if key == "actors":
                actors = {}
                for actor in value:
                    actors[actor] = Save._class_to_dict(actor)
                result = actors

            if key == "components":
                components = {}
                for component in value:
                    components[component] = Save._class_to_dict(component)
                result = components

            else:
                result = value
            print(result)
            result_dict[key] = result

        return result_dict


class Load:
    def level_load(loadpath, loadname):
        with open(os.path.join(loadpath, loadname), "r") as file:
            lines = file.readlines()
        file.close()
