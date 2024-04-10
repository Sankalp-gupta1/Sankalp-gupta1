import turtle
import time
import requests
from PIL import Image
from io import BytesIO

def display_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def draw_heart():
    print("Drawing heart...")
    welcome = turtle.Turtle()
    welcome.color("white")
    welcome.penup()
    welcome.setpos(-200, 200)
    welcome.write("Welcome to Starbucks", font=("Arial", 24, "bold"))
    welcome.hideturtle()

    heart = turtle.Turtle()
    heart.color("red")
    heart.fillcolor("red")
    heart.penup()
    heart.setpos(0, -200)
    heart.begin_fill()
    heart.left(140)
    heart.forward(224)
    for _ in range(200):
        heart.right(1)
        heart.forward(2)
    heart.left(120)
    for _ in range(200):
        heart.right(1)
        heart.forward(2)
    heart.forward(224)
    heart.end_fill()
    heart.hideturtle()

def draw_menu():
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set background color to black
    
    menu = turtle.Turtle()
    menu.color("dark green")  # Set menu text color to dark green
    menu.penup()
    menu.setpos(-200, 150)
    menu.write("MENU", font=("Arial", 24, "bold"))
    menu.setpos(-200, 100)
    menu.write("1. Latte", font=("Arial", 18))
    menu.setpos(-200, 70)
    menu.write("2. Cappuccino", font=("Arial", 18))
    menu.setpos(-200, 40)
    menu.write("3. Espresso", font=("Arial", 18))
    menu.setpos(-200, 10)
    menu.write("4. Black Iced Velvet", font=("Arial", 18))
    menu.setpos(-200, -20)
    menu.write("5. Chocolate Coffee", font=("Arial", 18))
    menu.setpos(-200, -50)
    menu.write("6. Ruby Grapefruit", font=("Arial", 18))
    menu.setpos(-200, -80)
    menu.write("7. Cake", font=("Arial", 18))
    menu.hideturtle()

def prompt_for_choice():
    choice = turtle.textinput("Menu Selection", "Please select an option (1-7): ")
    return choice

def make_latte():
    display_image_from_url("https://imgstaticcontent.lbb.in/lbbnew/wp-content/uploads/sites/2/2016/09/Starbucks-i.jpg")
    print("Here is your Latte! Enjoy!")

def make_cappuccino():
    display_image_from_url("https://insanelygoodrecipes.com/wp-content/uploads/2023/06/Cappuccino-Coffee-in-a-White-Cup.jpg")
    print("Here is your Cappuccino! Enjoy!")

def make_espresso():
    display_image_from_url("https://img.etimg.com/thumb/width-1200,height-1200,imgsize-92026,resizemode-75,msid-100057877/industry/services/retail/tata-starbucks-eyeing-strong-growth.jpg")
    print("Here is your Espresso! Enjoy!")

def make_black_iced_velvet():
    display_image_from_url("https://www.theflowerspoint.com/data/cache/images/cakes/cake%20by%20flavour/chocolate%20cake/dark-chocolate-Decorated-Cake-441x441.jpg")
    print("Here is your Black Iced Velvet! Enjoy!")

def make_chocolate_coffee():
    display_image_from_url("https://i.pinimg.com/originals/02/83/ae/0283ae4aa09289ec3ca652706cc30896.jpg")
    print("Here is your Chocolate Coffee! Enjoy!")

def make_ruby_grapefruit():
    display_image_from_url("https://i.redd.it/i92o76i33d5b1.jpg")
    print("Here is your Ruby Grapefruit! Enjoy!")

def make_cake():
    display_image_from_url("https://cakexpo-images.s3.ap-south-1.amazonaws.com/wp-content/uploads/2021/12/14050538/Screenshot_20211109-203525__02.jpg")
    print("Here is your Red Velvet Cake! Enjoy!")

def main():
    draw_heart()
    draw_menu()

    selected_items = []  # List to store selected items

    while True:
        choice = prompt_for_choice()
        if choice == "1":
            make_latte()
            selected_items.append("Latte")
        elif choice == "2":
            make_cappuccino()
            selected_items.append("Cappuccino")
        elif choice == "3":
            make_espresso()
            selected_items.append("Espresso")
        elif choice == "4":
            make_black_iced_velvet()
            selected_items.append("Black Iced Velvet")
        elif choice == "5":
            make_chocolate_coffee()
            selected_items.append("Chocolate Coffee")
        elif choice == "6":
            make_ruby_grapefruit()
            selected_items.append("Ruby Grapefruit")
        elif choice == "7":
            make_cake()
            selected_items.append("Cake")
        else:
            print("Invalid choice. Please select again.")

        time.sleep(2)  # Give some time to see the displayed image before clearing the screen
        turtle.clear()  # Clear the screen for the next iteration
        draw_menu()  # Redraw the menu

        if turtle.textinput("Continue?", "Do you want to select another item? (yes/no): ").lower() != "yes":
            break  # Break out of the loop if the user doesn't want to continue selecting items

    print("You selected the following items:")
    for item in selected_items:
        print("-", item)

    turtle.done()

if __name__ == "__main__":
    main()
