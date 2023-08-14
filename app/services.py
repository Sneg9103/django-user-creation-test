import os
import json

from migrations.models import Good


def populate_goods() -> None:
    """
    Populate the Good table with data from a JSON file.

    If duplicates are not allowed and the table is already populated,
    the function will simply return without adding any new goods.

    Args:
        allow_duplicates (bool): A flag indicating if duplicates are allowed. Defaults to False.
    """
    try:
        file_path = os.path.join("data", "goods.json")
        with open(file_path, "r") as file:
            goods_data = json.load(file)
            
        goods_to_insert = [
            Good(
                good_name=item["good_name"],
                good_code=item["good_code"],
                supplier_name=item["supplier_name"],
                supplier_address=item["supplier_address"],
                supplier_phone=item["supplier_phone"],
                supplier_contact=item["supplier_contact"],
                is_bulk=item["is_bulk"],
                price=item["price"],
                dt_of_license=item["dt_of_license"]
            )
            for item in goods_data
        ]

        Good.objects.bulk_create(goods_to_insert)
    
    except FileNotFoundError:
        raise FileNotFoundError("goods.json file not found")
    except json.decoder.JSONDecodeError:
        raise json.decoder.JSONDecodeError("goods.json file is malformed")
    except Exception as e:
        raise e
