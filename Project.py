from pyscript import document


def say_hello(e):
    visitor_name = document.getElementById("visitor_name").value.strip()

    if visitor_name:
        message = f"Hi, {visitor_name}! Thanks for visiting my page."
    else:
        message = "Hi! Thanks for visiting my page."

    document.getElementById("greeting").textContent = message
