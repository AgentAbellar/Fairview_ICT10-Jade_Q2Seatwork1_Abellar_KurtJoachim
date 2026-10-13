from pyscript import document, display

def checkMem(e):
    list = ["Alexander Floro", "Prince Villianueva", "Mira Gille", "Gavin Taguiga", "Jose Marie Macaya"]
    First= ["Alexander", "Prince", "Mira", "Gavin", "Jose Marie"]
    Last= ["Floro", "Villianueva", "Gille", "Taguiga", "Macaya"]
    members= [
        ("Alexander", "Floro"),
        ("Prince", "Villianueva"),
        ("Mira", "Gille"),
        ("Gavin", "Taguiga"),
        ("Jose Marie", "Macaya"),
    ]
    num1= document.getElementById("num1").value.strip
    num2= document.getElementById("num2").value.strip

    name = "KurtPanda"
    
    if (num1, num2) in members:
        message = f"Yipee user, you're in the club!"
    else:
        message = f"Sorry user, you're not in the club."

        document.getElementById("output1").innerText = message