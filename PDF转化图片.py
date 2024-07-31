import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import fitz  # PyMuPDF
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def pdf_to_images(pdf_path, output_folder):
    # 打开PDF文件
    pdf_document = fitz.open(pdf_path)
    
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历PDF的每一页
    for page_num in range(pdf_document.page_count):
        # 获取页面
        page = pdf_document.load_page(page_num)
        
        # 将页面转换为图片
        pix = page.get_pixmap()
        
        # 保存图片
        output_image_path = os.path.join(output_folder, f'page_{page_num + 1}.png')
        pix.save(output_image_path)
    
    messagebox.showinfo("完成", f"所有页面的图片已保存到文件夹: {output_folder}")

def select_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        pdf_entry.delete(0, tk.END)
        pdf_entry.insert(0, pdf_path)

def select_output_folder():
    output_folder = filedialog.askdirectory()
    if output_folder:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, output_folder)

def convert():
    pdf_path = pdf_entry.get()
    output_folder = output_entry.get()
    if pdf_path and output_folder:
        pdf_to_images(pdf_path, output_folder)
    else:
        messagebox.showwarning("警告", "请指定PDF文件和输出文件夹。")

# 创建GUI
root = tk.Tk()
root.title("PDF 转 图片")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

pdf_label = tk.Label(frame, text="选择PDF文件:")
pdf_label.grid(row=0, column=0, pady=5)

pdf_entry = tk.Entry(frame, width=50)
pdf_entry.grid(row=0, column=1, pady=5)

pdf_button = tk.Button(frame, text="浏览", command=select_pdf)
pdf_button.grid(row=0, column=2, pady=5)

output_label = tk.Label(frame, text="选择输出文件夹:")
output_label.grid(row=1, column=0, pady=5)

output_entry = tk.Entry(frame, width=50)
output_entry.grid(row=1, column=1, pady=5)

output_button = tk.Button(frame, text="浏览", command=select_output_folder)
output_button.grid(row=1, column=2, pady=5)

convert_button = tk.Button(frame, text="转换", command=convert)
convert_button.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
