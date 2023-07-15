import tkinter as tk
from tkinter import messagebox
import random
import configparser

class RandomNameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("随机点名程序")
        
        self.names = self.load_names()
        self.weights = self.load_weights()
        self.name = tk.StringVar()
        
        self.name_label = tk.Label(self.root, textvariable=self.name, font=("Arial", 20), padx=20, pady=20)
        self.name_label.pack()
        
        self.pick_button = tk.Button(self.root, text="抽取By VK", command=self.pick_name)
        self.pick_button.pack(pady=10)
        
        self.reset_button = tk.Button(self.root, text="重新抽取", command=self.pick_name)
        self.reset_button.pack(pady=10)
        
        self.root.mainloop()
        
    def load_names(self):
        config = configparser.ConfigParser()
        try:
            config.read('names.ini')
            return list(config.sections())
        except Exception as e:
            messagebox.showerror("错误", str(e))
            return []
    
    def load_weights(self):
        weights = {}
        config = configparser.ConfigParser()
        try:
            config.read('names.ini')
            for section in config.sections():
                weights[section] = config.getint(section, 'weight')
        except Exception as e:
            messagebox.showerror("错误", str(e))
        
        return weights
    
    def pick_name(self):
        if not self.names:
            messagebox.showerror("错误", "没有可抽取的元素！")
            return
        
        total_weight = sum(self.weights.values())
        num = random.randint(1, total_weight)
        
        for name in self.names:
            num -= self.weights[name]
            if num <= 0:
                self.name.set(name)
                break

root = tk.Tk()
app = RandomNameApp(root)
