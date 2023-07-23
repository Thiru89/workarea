class Car:
    brand_name = "BMW"
    model = "24"
    manu_year = "2020"

    def __init__(self, brand_name, model, manu_year):
        self.brand_name = brand_name
        self.model = model
        self.manu_year = manu_year

    def car_details(self):
        print(f"brand_name :{self.brand_name}")
        print(f"brand_name :{self.model}")
        print(f"brand_name :{self.manu_year}")

    def get_car_brand(self):
        return f"Car Brand is {self.brand_name}"

    def get_car_model(self):
        return f"Car Model Name is {self.model}"

    def get_car_manu_year(self):
        return f"Car Model Name is {self.manu_year}"


