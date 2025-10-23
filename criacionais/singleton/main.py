from . import singleton

def main():
    @singleton
    class  DatabaseConnection:
        def __init__(self, name: str):
            self.name = name
        
    db1 = DatabaseConnection("PrimaryDB")
    db2 = DatabaseConnection("SecondaryDB")

    print(f"DB1 Name: {db1.name}")
    print(f"DB2 Name: {db2.name}")

    print(f"DB1 is DB2: {db1 is db2}")

    print("\n ---  Renaming DB2 to 'SecondaryDB' ---")
    db2.name = "SecondaryDB"
    print(f"DB1 Name: {db1.name}")
    print(f"DB2 Name: {db2.name}")
    
if __name__ == "__main__":
    main()