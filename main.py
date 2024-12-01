import cv2
import pyvirtualcam
import os
import sys
from tkinter import Tk, Label, Button, filedialog, messagebox, Toplevel
from PIL import Image, ImageTk
import webbrowser

class VirtualCamApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cam Emulator")
        self.video_file = None
        self.cap = None
        self.cam = None

        # GUI Layout
        self.label = Label(root, text="No video selected", font=("Arial", 14))
        self.label.pack(pady=20)

        self.preview = Label(root)
        self.preview.pack()

        self.select_btn = Button(root, text="Select Video", command=self.select_video)
        self.select_btn.pack(pady=10)

        self.start_btn = Button(root, text="Start Virtual Camera", command=self.start_camera, state="disabled")
        self.start_btn.pack(pady=10)

        self.stop_btn = Button(root, text="Stop", command=self.stop_camera, state="disabled")
        self.stop_btn.pack(pady=10)

        self.donate_btn = Button(root, text="Donate", command=self.show_donation)
        self.donate_btn.pack(pady=10)

        self.creator_btn = Button(root, text="About the Creator", command=self.show_creator)
        self.creator_btn.pack(pady=10)

    def select_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv;*.mov")])
        if file_path:
            self.video_file = file_path
            self.label.config(text=f"Selected: {os.path.basename(file_path)}")
            self.start_btn.config(state="normal")

    def start_camera(self):
        if not self.video_file:
            messagebox.showerror("Error", "No video file selected.")
            return

        self.cap = cv2.VideoCapture(self.video_file)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Could not open video file.")
            return

        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))

        try:
            self.cam = pyvirtualcam.Camera(width=width, height=height, fps=fps, print_fps=True)
            self.label.config(text="Virtual camera started.")
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.stream_frames()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start virtual camera: {e}")
            self.cap.release()

    def stream_frames(self):
        if self.cap is None or not self.cap.isOpened():
            return

        ret, frame = self.cap.read()
        if not ret:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
            return self.root.after(10, self.stream_frames)

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Update preview
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)
        self.preview.imgtk = imgtk
        self.preview.config(image=imgtk)

        # Send frame to virtual camera
        self.cam.send(frame_rgb)
        self.cam.sleep_until_next_frame()

        # Loop
        self.root.after(10, self.stream_frames)

    def stop_camera(self):
        if self.cap:
            self.cap.release()
            self.cap = None
        if self.cam:
            self.cam.close()
            self.cam = None
        self.label.config(text="Stopped.")
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.preview.config(image="")

    def show_donation(self):
        donation_window = Toplevel(self.root)
        donation_window.title("Donate to Support")

        Label(donation_window, text="Support our work by donating!", font=("Arial", 14)).pack(pady=10)

        # Your UPI ID
        upi_id = "credmemishra@fam"
        Label(donation_window, text=f"UPI ID: {upi_id}", font=("Arial", 12), fg="blue").pack(pady=10)

        Button(donation_window, text="Copy UPI ID", command=lambda: self.copy_to_clipboard(upi_id)).pack(pady=10)
        Button(donation_window, text="Close", command=donation_window.destroy).pack(pady=10)

    def copy_to_clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()  # Required for clipboard to work
        messagebox.showinfo("Copied", "UPI ID copied to clipboard!")

    def show_creator(self):
        creator_window = Toplevel(self.root)
        creator_window.title("About the Creator")

        Label(creator_window, text="Cam Emulator", font=("Arial", 16, "bold")).pack(pady=10)
        Label(creator_window, text="Created by: @ma290", font=("Arial", 14)).pack(pady=10)

        Button(creator_window, text="Visit GitHub Profile", command=lambda: webbrowser.open("https://github.com/ma290")).pack(pady=10)
        Button(creator_window, text="Close", command=creator_window.destroy).pack(pady=10)

    def on_close(self):
        self.stop_camera()
        self.root.destroy()

# Main Application
if __name__ == "__main__":
    root = Tk()
    app = VirtualCamApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
