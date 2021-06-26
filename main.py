#DONT ROAST ME CODE.
import pyscreenshot
import tkinter as tk

qs = input("Fullscreen or Custom size [F/C]: ")


if qs == "F":
    image = pyscreenshot.grab(bbox=(0, 0, 1920, 1080))
    image.show()
    saveornot = input("Do you want to save that image? [Y/N]: ")
    if saveornot == "Y":
        nameforfile = input("What do you want to name the image?: ")
        image.save(str(nameforfile+".png"))
        print("Saved!")
    elif saveornot == "N":
        print("Bye!")
    else:
        print("Bleh, Check your input again.")    

elif qs == "C":
    print("")
    print("####################################")
    print("Could be a mess typing out the resolution, but hey it works.\nIf its a specific window you want to capture bring the application towards\nthe top left of the screen")
    print("####################################")
    print("")
    sizex = input("Width of the screen to be taken: ")
    sizey = input("Lenght of the screen to be taken: ")
    location = input("Do you want to specify which part of the screen to be captured?(Default: 0,0)[Y/N]:")
    if location == "Y":
        fromxaxis = input("From X axis: ")
        fromyaxis = input("From Y axis: ")
        root = tk.Tk()
        b = sizex+"x"+sizey
        print("")
        print("####################################")
        print("A new window should have poppep up.\nIt is showing a sample of the size that is going to be captured.\nClose it to continue") 
        print("####################################")
        print("")
        root.title("Close me to capture the shot.")
        root.geometry(b)
        root.mainloop()
        image = pyscreenshot.grab(bbox=(int(fromxaxis), int(fromyaxis), int(sizex), int(sizey)))
        image.show()
        saveornot = input("Do you want to save that image? [Y/N]: ")
        if saveornot == "Y":
            nameforfile = input("What do you want to name the image?: ")
            image.save(str(nameforfile +".png"))
            print("Saved!")
        elif saveornot == "N":
            print("Bye!")

    elif location == "N":    

        b = sizex+"x"+sizey
        root = tk.Tk()
        print("")
        print("####################################")
        print("A new window should have poppep up.\nIt is showing a sample of the size that is going to be captured.\nClose it to continue") 
        print("####################################")
        print("")
        root.title("Close me to capture the shot.")
        root.geometry(b)
        root.mainloop()
 
        image = pyscreenshot.grab(bbox=(0, 0, int(sizex), int(sizey)))
        image.show()
        saveornot = input("Do you want to save that image? [Y/N]: ")
        if saveornot == "Y":
            nameforfile = input("What do you want to name the image?: ")
            image.save(str(nameforfile +".png"))
            print("Saved!")
        elif saveornot == "N":
            print("Bye!")   
else:
    print("Bleh, check your input again.")
#DONT ROAST MY CODE.    


    
    

