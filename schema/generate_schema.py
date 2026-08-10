import json
import os

from database import Database


OUTPUT_FILE = os.path.join(
    os.path.dirname(__file__),
    "schema.json"
)



def get_tables(db):

    result = db.execute_select(
        "SHOW TABLES"
    )

    tables = []

    for table in result:

        tables.append(
            list(table.values())[0]
        )

    return tables



def get_columns(db, table_name):

    result = db.execute_select(
        f"SHOW COLUMNS FROM `{table_name}`"
    )


    columns = []


    for column in result:

        columns.append(
            {
                "name": column["Field"],
                "type": column["Type"],
                "nullable": column["Null"],
                "key": column["Key"],
                "default": column["Default"],
                "extra": column["Extra"]
            }
        )


    return columns



def generate_schema():

    db = Database()


    schema = {
        "tables": {}
    }


    tables = get_tables(db)


    print(
        f"📌 {len(tables)} tables trouvées"
    )


    for table in tables:

        print(
            "Analyse :",
            table
        )


        schema["tables"][table] = {
            "columns": get_columns(
                db,
                table
            )
        }



    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            schema,
            file,
            indent=4,
            ensure_ascii=False
        )


    print(
        "✅ schema.json généré :",
        OUTPUT_FILE
    )


    db.close()



if __name__ == "__main__":

    generate_schema()