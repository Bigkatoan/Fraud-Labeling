from preprocess import gen_label
from customtkinter import *
from PIL import Image

if __name__ == "__main__":
    gen_label()
    app = CTk()
    app.geometry("1280x720")
    images = os.listdir('pltimages/')
    frame = CTkFrame(master=app, fg_color="#BED7DC", height=640)
    frame.pack(expand=True)
    frame.place(relx=.1, rely=.5, anchor="center")
    imgframe = CTkFrame(master=app, fg_color="#BED7DC")
    imgframe.pack(expand=True)
    imgframe.place(relx=.6, rely=.5, anchor="center")
    index = 0

    def press():
        global list_check_boxs, index
        p = False
        try:
            save_str = [str(val.get()) for val in list_check_boxs]
        except:
            list_check_boxs = []
            p = True
        if not p:
            save_str = ' '.join(save_str)
            print(save_str)
            with open(f'fraud/img_{index}.txt', 'w') as f:
                f.write(save_str)
            print('write complete')
            index += 1

        if len(images) == 0:
            app.quit()
            return
        
        for widget in frame.winfo_children():
            widget.destroy()

        for widget in imgframe.winfo_children():
            widget.destroy()

        img_path = images.pop(0)
        with open('labels/' + img_path.split('.')[0] + '.txt', 'r') as f:
            data = f.readlines()

        img = CTkImage(dark_image=Image.open('pltimages/' + img_path), size=(640,640))
        my_label = CTkLabel(imgframe, text="", image=img)
        my_label.pack(pady=10)

        list_check_boxs = []
        data = [val.split(' ') for val in data]
        for i in range(len(data)):
            chb = CTkCheckBox(master=frame, 
                            text=f"person: {i}", 
                            text_color="#153448")
            chb.pack(expand=True, padx=30, pady=20)
            list_check_boxs.append(chb)

    next_button = CTkButton(master=app, text='next', command=press)
    next_button.place(relx=0.9, 
                    rely=0.95, 
                    anchor="center")

    app.mainloop()