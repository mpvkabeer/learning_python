# Import the Student class and calculate_average function from the module inside the package
from seller import Seller
from utils import write_data_to_excel

def main():
    sellers_dict_array = [
        { "id": 1, "name": "Anand", "profits": {"q1": 500000, "q2": 5000, "q3": 500000, "q4": 5000} },
        { "id": 2, "name": "Bob", "profits": {"q1":5000, "q2": 6000,  "q3": 6000, "q4": 6000} },
        { "id": 3, "name": "Cedric", "profits": {"q1":250000, "q2": 5000,  "q3": 5000, "q4": 5000} },
        { "id": 4, "name": "Devi", "profits": {"q1":600000, "q2": 5000,  "q3": 4000, "q4": 7800} },
    ]

    sellers_array = []

    for seller_data in sellers_dict_array:
        seller = Seller(seller_data["id"], seller_data["name"], seller_data["profits"])
        #seller.seller_id = seller_data["id"]
        seller.calculate_and_set_reward()
        sellers_array.append(seller)

    for seller_obj in sellers_array:
        seller_obj.display_info()

    write_data_to_excel(sellers_array)

if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
