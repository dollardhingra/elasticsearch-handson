import os
import json
import random

def run():
    random_images = [
        "https://images.pexels.com/photos/4460725/pexels-photo-4460725.jpeg?cs=srgb&dl=pexels-deepak-digwal-4460725.jpg&fm=jpg",
        "https://images.pexels.com/photos/4654782/pexels-photo-4654782.jpeg?cs=srgb&dl=pexels-jacob-pilatoe-4654782.jpg&fm=jpg",
        "https://images.pexels.com/photos/4320368/pexels-photo-4320368.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        "https://images.pexels.com/photos/3758105/pexels-photo-3758105.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260"
        "https://images.pexels.com/photos/1181345/pexels-photo-1181345.jpeg?cs=srgb&dl=pexels-christina-morillo-1181345.jpg&fm=jpg",
        "https://images.pexels.com/photos/4680619/pexels-photo-4680619.jpeg?cs=srgb&dl=pexels-skyler-ewing-4680619.jpg&fm=jpg",
        "https://images.pexels.com/photos/5213716/pexels-photo-5213716.jpeg?cs=srgb&dl=pexels-kebs-visuals-5213716.jpg&fm=jpg",
        "https://images.pexels.com/photos/5378413/pexels-photo-5378413.jpeg?cs=srgb&dl=pexels-barna-david-5378413.jpg&fm=jpg"
    ]
    # Load the product json from the same directory as this file.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    products_path = os.path.join(dir_path, 'products.json')
    with open(products_path, mode="r") as product_file:
        data = json.load(product_file)
        for product in data:
            product["image"] = random.choice(random_images)

    os.remove(products_path)
    with open(products_path, 'w') as product_file:
        json.dump(data, product_file, indent=4)

run()