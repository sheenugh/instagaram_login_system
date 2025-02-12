# || DEFECTS ||
# - "Invalid username and password" does not pop up in the messagebox showerror when both username and pass are incorrect or not registered, instead it only pops up as "Invalid username."
# - After exiting the messagebox " all fields are required", chars in the username and pass are not remove

# || CONTENT || 
# - When user inputs an invalid username, invalid password, or invalid username and password, it shows either of the "Invalid password" or "Invalid username".
# - TOkito username will successfully logged in without an after music and lyrics.
# - In addition, when user successfully logged in to miss_you_... it plays the song and the lyrics. 




# || IMPORTS ||
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pygame

# || CLASS ||
class InstagramLoginSystemComponents:
    def __init__(self, root):
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Load sound files
        try:
            # Default success sound (you may want to use a silent file or just avoid playing sound for tokito_muichir0)
            self.default_success_sound = pygame.mixer.Sound("miss_miss.mp3")
            # Specific success sound for the given username
            self.special_success_sound = pygame.mixer.Sound("miss_miss.mp3")  # Ensure you have a special sound file
        except pygame.error as e:
            print(f"Error loading sound file: {e}")
            return
        
        # - Instance Variables
        self.root = root
        self.root.title("Instagram Login")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#fafafa")

        # - Adding image
        accessing_system_home_image = Image.open("Images/login_system_photo (3).png")
        resized_system_home_image = accessing_system_home_image.resize((500, 650))
        self.system_home_image_access_by_photoimage = ImageTk.PhotoImage(resized_system_home_image)
        self.adding_system_home_image_in_the_window = Label(self.root, image=self.system_home_image_access_by_photoimage, bd=0).place(x=200, y=50)

        # - Login Frame
        system_login_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        system_login_frame.place(x=660, y=140, width=380, height=395)

        # - Title of Login Frame
        title = Label(system_login_frame, text="Instagram", font=("Elephant", 28, "bold"), bg="white").place(x=0, y=30, relwidth=1)

        # - Username Label and Entry
        username_label = Label(system_login_frame, text="Username, phone number, or email", font=("Andalus", 12), bg="white", fg="#767171").place(x=50, y=110)
        self.username = StringVar()
        username_entry = Entry(system_login_frame, textvariable=self.username, font=("times new roman", 14), bg="#ECECEC").place(x=50, y=135, width=280)

        # - Password Label and Entry
        password_label = Label(system_login_frame, text="Password", font=("Andalus", 12), bg="white", fg="#767171").place(x=50, y=175)
        self.password = StringVar()
        password_entry = Entry(system_login_frame, textvariable=self.password, font=("times new roman", 14), bg="#ECECEC", show="*").place(x=50, y="200", width=280)

        # - Button Login
        login_button = Button(system_login_frame, text="Log in", font=("Arial Rounded MT Bold", 15), bg="dodgerblue", activebackground="dodgerblue", activeforeground="white", fg="white", cursor="hand2", command=self.login).place(x=50, y=250, width=280, height=35)

        # - Optional Text
        or_text = Label(system_login_frame, bg="lightgray").place(x=50, y=310, width=280, height=2)
        or_label = Label(system_login_frame, text="OR", font=("times new roman", 11, "bold"), bg="white", fg="lightgray").place(x=175, y=300)

        # - Forgot Password Button
        self.forgot_password_button = Button(system_login_frame, text="Forgot Password?", font=("times new roman", 12, "bold"), bg="white", fg="#007BFF", bd=0, activebackground="white", activeforeground="#007BFF")
        self.forgot_password_button.place(x=125, y=330)
        self.forgot_password_button.bind("<Enter>", self.on_hover)
        self.forgot_password_button.bind("<Leave>", self.on_leave)

        # - Don't have an account frame
        dac_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        dac_frame.place(x=660, y=550, width=380, height=45)

        # - Don't have an account text
        self.dac_label = Label(dac_frame, text="Don't have an account?", font=("times new roman", 11), bg="white").place(x=80, y=10)

        # - Sign up label
        self.sign_up_label = Button(dac_frame, text="Sign up", font=("times new roman", 11, "bold"), bg="white", fg="#007BFF", activebackground="white", activeforeground="#007BFF", bd=0)
        self.sign_up_label.place(x=220, y=9.5)
        self.sign_up_label.bind("<Enter>", self.on_hover)
        self.sign_up_label.bind("<Leave>", self.on_leave)

        # Images for the animation
        self.image_size = (254, 356)  # Size for animation
        self.photos = [
            self.resize_image("Images/lgn_illu_img1.png"),
            self.resize_image("Images/lgn_illu_img2.png"),
            self.resize_image("Images/lgn_illu_img3.png"),
            self.resize_image("Images/OPL_im5.jpg"),
            self.resize_image("Images/OPL_im6.png"),
            self.resize_image("Images/gojo_im7.jpg"),
            self.resize_image("Images/ig_post_img8.jpg"),
        ]

        self.label_change_image = Label(self.root, bg="white")
        self.label_change_image.place(x=370, y=187, width=self.image_size[0], height=self.image_size[1])

        self.current_image_index = 0
        self.animate_images()

        # Sample lyrics
        self.lyrics = [
            "..........\n"
            "Magaan na ba ang 'yong paghinga\n"
            "bumalik ka na sa'kin\n"
            "..........\n"
            "Klaro na ba ang isip sinta\n"
            "bumalik ka na sa'kin :("
        ]
        
        self.typing_speed = 120  # Speed of typing in milliseconds
        self.line_delay = 3000  # Delay between lines in milliseconds
        
    # - Resizing the images to fit
    def resize_image(self, path):
        image = Image.open(path)
        image = image.resize(self.image_size)
        return ImageTk.PhotoImage(image)

    # - For the animation of the images
    def animate_images(self):
        self.label_change_image.config(image=self.photos[self.current_image_index])
        self.current_image_index = (self.current_image_index + 1) % len(self.photos)
        self.label_change_image.after(2000, self.animate_images)

    # - For underline when the cursor is placed on the text
    def on_hover(self, event):
        widget = event.widget
        current_font = widget.cget("font")
        new_font = self._add_underline(current_font)
        widget.config(font=new_font)

    def on_leave(self, event):
        widget = event.widget
        current_font = widget.cget("font")
        new_font = self._remove_underline(current_font)
        widget.config(font=new_font)

    def _add_underline(self, font):
        return font + " underline"

    def _remove_underline(self, font):
        return font.replace(" underline", "")

    # - Stop sound
    def stop_sound(self):
        pygame.mixer.stop()

    # - Login condition statement
    def login(self):
        username = self.username.get().strip()
        password = self.password.get().strip()

        # Check if any field is empty
        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return  # Exit the method if any field is empty

        # Validate username and password
        valid_credentials = {
            "tokito_muichir0": "Magandasisheena16!",
            "miss_you_uWu": "12345!"
        }

        if username in valid_credentials:
            if password == valid_credentials[username]:
                # Successful login
                messagebox.showinfo("Login Successful", "You have logged in successfully!")
                
                # Play sound and show lyrics based on username
                if username == "miss_you_uWu":
                    print("Login successful with special username. Playing special sound.")
                    self.special_success_sound.play()
                    self.lyrics = [
                        "Oh.............\n"
                        "Magkita na tayo please T_T \n"
                        "......\n"
                        "Palagi kang nami-miss :(\n"
                        "...............\n"
                        "Oh, oh\n"
                        ".................\n"
                        "Oh\n"
                        "......."
                        
                    ]
                    self.show_lyrics_window()
                else:
                    print("Login successful. No sound for this username.")
                    self.stop_sound()
                
                self.username.set("")
                self.password.set("")
            else:
                # Invalid password
                messagebox.showerror("Error", "Invalid password. Please try again.")
                self.username.set("")
                self.password.set("")
        else:
            # Invalid username
            messagebox.showerror("Error", "Invalid username. Please try again.")
            self.username.set("")
            self.password.set("")

    # - Show lyrics in a new window with typewriter effect
    def show_lyrics_window(self):
        lyrics_window = Toplevel(self.root)
        lyrics_window.title("Lyrics")
        lyrics_window.geometry("600x400")
        lyrics_window.config(bg="#fafafa")

        # Bind the window close event to stop the sound
        lyrics_window.protocol("WM_DELETE_WINDOW", self.on_closing_lyrics_window)

        lyrics_label = Label(lyrics_window, text="", font=("times new roman", 16), bg="#fafafa", fg="black")
        lyrics_label.pack(pady=20, padx=20)

        self.display_lyrics(lyrics_label, 0)
        self.lyrics_window = lyrics_window  # Keep a reference to the window

    def on_closing_lyrics_window(self):
        self.stop_sound()
        self.lyrics_window.destroy()

    def display_lyrics(self, label, line_index):
        if line_index < len(self.lyrics):
            text = self.lyrics[line_index]
            self.type_text(label, text, 0, lambda: self.root.after(self.line_delay, lambda: self.display_lyrics(label, line_index + 1)))

    def type_text(self, label, text, index, callback):
        if index < len(text):
            label.config(text=text[:index + 1])
            label.update()
            self.root.after(self.typing_speed, lambda: self.type_text(label, text, index + 1, callback))
        else:
            callback()

# - Host or main window of the tkinter application
root = Tk()

# - Object of the class
app = InstagramLoginSystemComponents(root)

# - Loop of the tkinter -- opens the window
root.mainloop()
