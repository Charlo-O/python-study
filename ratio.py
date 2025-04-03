import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import shutil
from pathlib import Path

class PhotoClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("照片比例分类器")
        self.root.geometry("1000x600")
        
        # 定义比例类别
        self.ratio_categories = {
            "2:1": (1.9, 2.1),    # 2:1 比例范围
            "3:2": (1.4, 1.6),    # 3:2 比例范围
            "20:9": (2.1, 2.3),   # 20:9 比例范围
            "1:2": (0.4, 0.6)     # 1:2 比例范围
        }
        
        # 保存图片的文件夹路径
        self.output_dir = None
        
        # 当前处理的图片
        self.current_images = []
        self.current_index = 0
        
        self.setup_ui()
    
    def setup_ui(self):
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 顶部控制区
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=10)
        
        # 选择图片按钮
        select_btn = ttk.Button(control_frame, text="选择图片", command=self.select_images)
        select_btn.pack(side=tk.LEFT, padx=5)
        
        # 添加选择文件夹按钮
        select_folder_btn = ttk.Button(control_frame, text="选择文件夹", command=self.select_folder)
        select_folder_btn.pack(side=tk.LEFT, padx=5)
        
        # 设置输出目录按钮
        output_btn = ttk.Button(control_frame, text="设置输出目录", command=self.set_output_dir)
        output_btn.pack(side=tk.LEFT, padx=5)
        
        # 开始分类按钮
        classify_btn = ttk.Button(control_frame, text="开始分类", command=self.classify_images)
        classify_btn.pack(side=tk.LEFT, padx=5)
        
        # 状态标签
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_label = ttk.Label(control_frame, textvariable=self.status_var)
        status_label.pack(side=tk.RIGHT, padx=5)
        
        # 创建图片展示区域
        preview_frame = ttk.LabelFrame(main_frame, text="图片预览")
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 图片画布
        self.canvas = tk.Canvas(preview_frame, bg="gray")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # 预览导航按钮
        nav_frame = ttk.Frame(main_frame)
        nav_frame.pack(fill=tk.X, pady=5)
        
        prev_btn = ttk.Button(nav_frame, text="上一张", command=self.show_previous)
        prev_btn.pack(side=tk.LEFT, padx=5)
        
        next_btn = ttk.Button(nav_frame, text="下一张", command=self.show_next)
        next_btn.pack(side=tk.LEFT, padx=5)
        
        # 图片信息
        self.info_var = tk.StringVar()
        self.info_var.set("未选择图片")
        info_label = ttk.Label(nav_frame, textvariable=self.info_var)
        info_label.pack(side=tk.LEFT, padx=20)
        
        # 分类结果显示区域
        result_frame = ttk.LabelFrame(main_frame, text="分类结果")
        result_frame.pack(fill=tk.X, pady=10)
        
        # 为每个比例类别创建一个标签
        self.category_counts = {}
        category_frame = ttk.Frame(result_frame)
        category_frame.pack(fill=tk.X, pady=5)
        
        for i, category in enumerate(self.ratio_categories.keys()):
            label = ttk.Label(category_frame, text=f"{category}: 0张图片")
            label.grid(row=0, column=i, padx=10)
            self.category_counts[category] = label
    
    def select_images(self):
        """选择多张图片"""
        filetypes = [
            ("图片文件", "*.jpg *.jpeg *.png *.bmp *.gif"),
            ("所有文件", "*.*")
        ]
        image_paths = filedialog.askopenfilenames(filetypes=filetypes)
        
        if image_paths:
            self.current_images = list(image_paths)
            self.current_index = 0
            self.status_var.set(f"已选择 {len(self.current_images)} 张图片")
            self.show_current_image()
    
    def select_folder(self):
        """选择包含图片的文件夹"""
        folder_path = filedialog.askdirectory(title="选择包含图片的文件夹")
        if not folder_path:
            return
        
        # 支持的图片扩展名
        supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
        
        # 获取文件夹中的所有图片
        image_paths = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(supported_extensions):
                    image_paths.append(os.path.join(root, file))
        
        if image_paths:
            self.current_images = image_paths
            self.current_index = 0
            self.status_var.set(f"已选择 {len(self.current_images)} 张图片")
            self.show_current_image()
        else:
            messagebox.showinfo("提示", "所选文件夹中没有找到支持的图片文件")
    
    def set_output_dir(self):
        """设置分类后图片的保存目录"""
        output_dir = filedialog.askdirectory()
        if output_dir:
            self.output_dir = output_dir
            self.status_var.set(f"输出目录: {self.output_dir}")
    
    def show_current_image(self):
        """显示当前索引的图片"""
        if not self.current_images:
            return
        
        image_path = self.current_images[self.current_index]
        self.info_var.set(f"图片 {self.current_index + 1}/{len(self.current_images)}: {os.path.basename(image_path)}")
        
        try:
            # 使用PIL打开图片
            img = Image.open(image_path)
            
            # 计算缩放比例以适应画布
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            
            if canvas_width <= 1 or canvas_height <= 1:  # 还未渲染完成，使用预估尺寸
                canvas_width = 800
                canvas_height = 400
            
            # 计算缩放比例
            img_width, img_height = img.size
            ratio = min(canvas_width / img_width, canvas_height / img_height)
            new_width = int(img_width * ratio)
            new_height = int(img_height * ratio)
            
            # 调整图片大小
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # 将PIL图像转换为Tkinter图像
            self.photo = ImageTk.PhotoImage(resized_img)
            
            # 清除画布并显示新图像
            self.canvas.delete("all")
            self.canvas.create_image(
                canvas_width // 2, canvas_height // 2,
                image=self.photo, anchor=tk.CENTER
            )
            
            # 显示图片比例
            aspect_ratio = img_width / img_height
            category = self.classify_ratio(aspect_ratio)
            self.canvas.create_text(
                canvas_width // 2, 20,
                text=f"比例: {aspect_ratio:.2f} ({category if category else '其他'})",
                fill="white", font=("Arial", 12)
            )
            
        except Exception as e:
            messagebox.showerror("错误", f"无法显示图片: {e}")
    
    def show_next(self):
        """显示下一张图片"""
        if self.current_images and self.current_index < len(self.current_images) - 1:
            self.current_index += 1
            self.show_current_image()
    
    def show_previous(self):
        """显示上一张图片"""
        if self.current_images and self.current_index > 0:
            self.current_index -= 1
            self.show_current_image()
    
    def classify_ratio(self, ratio):
        """根据长宽比例确定图片类别，寻找最接近的类别"""
        # 预定义的标准比例
        standard_ratios = {
            "2:1": 2.0,
            "3:2": 1.5,
            "20:9": 2.22,
            "1:2": 0.5
        }
        
        # 检查原始比例
        closest_category = None
        min_difference = float('inf')
        
        for category, std_ratio in standard_ratios.items():
            difference = abs(ratio - std_ratio)
            if difference < min_difference:
                min_difference = difference
                closest_category = category
        
        return closest_category
    
    def classify_images(self):
        """分类所有选中的图片"""
        if not self.current_images:
            messagebox.showinfo("提示", "请先选择图片")
            return
            
        if not self.output_dir:
            messagebox.showinfo("提示", "请设置输出目录")
            return
        
        # 创建分类目录 - 将冒号替换为下划线
        category_dirs = {}
        for category in self.ratio_categories.keys():
            # 将冒号替换为下划线，以便在Windows上创建有效的文件夹名
            folder_name = category.replace(':', '_')
            category_dir = os.path.join(self.output_dir, folder_name)
            os.makedirs(category_dir, exist_ok=True)
            category_dirs[category] = category_dir
        
        # 其他类别
        other_dir = os.path.join(self.output_dir, "其他")
        os.makedirs(other_dir, exist_ok=True)
        
        # 分类计数
        counts = {category: 0 for category in self.ratio_categories.keys()}
        other_count = 0
        
        # 处理每张图片
        for image_path in self.current_images:
            try:
                # 打开图片并获取其尺寸
                img = Image.open(image_path)
                width, height = img.size
                ratio = width / height
                
                # 确定图片类别
                category = self.classify_ratio(ratio)
                
                # 拷贝图片到对应目录
                filename = os.path.basename(image_path)
                
                if category:
                    dest_path = os.path.join(category_dirs[category], filename)
                    counts[category] += 1
                else:
                    dest_path = os.path.join(other_dir, filename)
                    other_count += 1
                
                shutil.copy2(image_path, dest_path)
                
            except Exception as e:
                messagebox.showerror("错误", f"处理图片 {image_path} 时出错: {e}")
        
        # 更新界面上的计数
        for category, count in counts.items():
            self.category_counts[category].config(text=f"{category}: {count}张图片")
        
        # 显示结果
        messagebox.showinfo("完成", f"图片分类完成！\n" + 
                          "\n".join([f"{category}: {count}张" for category, count in counts.items()]) +
                          f"\n其他: {other_count}张")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoClassifierApp(root)
    root.mainloop()
