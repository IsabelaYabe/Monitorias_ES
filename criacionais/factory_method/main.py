from . import Paint

def main():
    app = Paint()

    drawing = app.new_document("flower")
    drawing.content = "Very beautiful flower"
    drawing.colors = ["pink", "green"]

    print("\n--- OPENING DOCUMENT ---")
    app.open_document("flower")

    print("\n--- SAVING STATE ---")
    drawing.save()

    print("\n--- MODIFYING CONTENT ---")
    drawing.content = "Modified flower"
    drawing.colors.append("yellow")

    print(f"Current content: {drawing.content}")
    print(f"Current colors: {drawing.colors}")

    print("\n--- REVERTING STATE ---")
    drawing.revert()

    print(f"Content after revert: {drawing.content}")
    print(f"Colors after revert: {drawing.colors}")

    print("\n--- CLOSING DOCUMENT ---")
    app.close_document("flower")

if __name__ == "__main__":
    main()
