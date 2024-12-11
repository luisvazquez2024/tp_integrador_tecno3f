import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import ttkbootstrap as tb

# class Frame3(tb.Frame):
# 		def __init__(self, master=None):
# 			super().__init__(master)
# 			self.master = master
# 			self.pack()
# 			self.ventana_lista_producto()

# 		def ventana_lista_producto(self):
# 			self.frame_lista_producto = tb.Frame(self)
# 			self.frame_lista_producto.pack(padx=10, pady=10)

# 			self.lblfframe_tree_listprod = tb.LabelFrame(self.frame_lista_producto, text="Lista de Productos")
# 			self.lblfframe_tree_listprod.pack(padx=10, pady=10, fill="both", expand=True)

# 			columnas = ("codigo", "nombre", "stock", "precio", "origen", "tipo_producto")
# 			self.tree_lista_productos = tb.Treeview(self.lblfframe_tree_listprod, columns=columnas, height=17, show="headings")
# 			self.tree_lista_productos.pack(side="left", fill="both", expand=True)

# 			for col in columnas:
# 					self.tree_lista_productos.heading(col, text=col.capitalize(), anchor=tk.W)

# 			# Crear el scrollbar
# 			tree_scroll_lista_prod = tb.Scrollbar(self.lblfframe_tree_listprod, bootstyle="round-success")
# 			tree_scroll_lista_prod.pack(side="right", fill="y")
# 			tree_scroll_lista_prod.config(command=self.tree_lista_productos.yview)
# 			self.tree_lista_productos.config(yscrollcommand=tree_scroll_lista_prod.set)

# 			# Botones para agregar, actualizar y eliminar productos
# 			btn_agregar = tb.Button(self.frame_lista_producto, text="Agregar Producto", command=self.ventana_agregar_producto)
# 			btn_agregar.pack(pady=5)

# 			btn_actualizar = tb.Button(self.frame_lista_producto, text="Actualizar Producto", command=self.ventana_actualizar_producto)
# 			btn_actualizar.pack(pady=5)

# 			btn_eliminar = tb.Button(self.frame_lista_producto, text="Eliminar Producto", command=self.eliminar_producto)
# 			btn_eliminar.pack(pady=5)

# 			# Llamamos a nuestra función para mostrar productos
# 			self.mostrar_productos()



# 		def mostrar_productos(self):
# 			try:
# 					conexion = sqlite3.connect("sistema.db")
# 					cur = conexion.cursor()
# 					registros = self.tree_lista_productos.get_children()
# 					for e in registros:
# 							self.tree_lista_productos.delete(e)

# 					cur.execute("SELECT * FROM productos ORDER BY codigo DESC;")
# 					datos = cur.fetchall()
# 					for row in datos:
# 							self.tree_lista_productos.insert("", "end", values=row)

# 					conexion.commit()
# 			except sqlite3.Error as e:
# 					messagebox.showerror("Lista de Productos", f"Ocurrió un error al mostrar los productos: {e}")
# 			finally:
# 					conexion.close()

# 		def ventana_agregar_producto(self):
# 				self.ventana_producto = tk.Toplevel(self)
# 				self.ventana_producto.title("Agregar Producto")
# 				self.ventana_producto.geometry("300x300")

# 				# Entradas para los detalles del producto
# 				tk.Label(self.ventana_producto, text="Código").pack(pady=5)
# 				self.txt_codigo = ttk.Entry(self.ventana_producto)
# 				self.txt_codigo.pack(pady=5)

# 				tk.Label(self.ventana_producto, text="Nombre").pack(pady=5)
# 				self.txt_nombre = ttk.Entry(self.ventana_producto)
# 				self.txt_nombre.pack(pady=5)

# 				tk.Label(self.ventana_producto, text="Stock").pack(pady=5)
# 				self.txt_stock = ttk.Entry(self.ventana_producto)
# 				self.txt_stock.pack(pady=5)

# 				tk.Label(self.ventana_producto, text="Precio").pack(pady=5)
# 				self.txt_precio = ttk.Entry(self.ventana_producto)
# 				self.txt_precio.pack(pady=5)

# 				tk.Label(self.ventana_producto, text="Origen").pack(pady=5)
# 				self.txt_origen = ttk.Entry(self.ventana_producto)
# 				self.txt_origen.pack(pady=5)

# 				tk.Label(self.ventana_producto, text="Tipo de Producto").pack(pady=5)
# 				self.txt_tipo = ttk.Entry(self.ventana_producto)
# 				self.txt_tipo.pack(pady=5)
			
# 				btn_guardar = tb.Button(self.ventana_producto, text="Guardar", command=self.guardar_producto)
# 				btn_guardar.pack(pady=10)

# 				import tkinter as tk


class Frame3(tb.Frame):
		def __init__(self, root=None):
				super().__init__(root)
				self.root = root
				self.pack()
				self.ventana_lista_producto()

		def ventana_lista_producto(self):
			self.frame_lista_producto = ttk.Frame(self)
			self.frame_lista_producto.pack(padx=10, pady=10)

			# Treeview para mostrar productos
			self.tree_lista_productos = ttk.Treeview(self.frame_lista_producto, columns=("Código", "Nombre", "Stock", "Precio", "Origen", "Tipo"), show='headings')
			self.tree_lista_productos.grid(row=0, column=0, columnspan=3)

			# Definir encabezados
			for col in self.tree_lista_productos['columns']:
					self.tree_lista_productos.heading(col, text=col)

			# Botones para agregar, actualizar y eliminar productos
			btn_agregar = tb.Button(self.frame_lista_producto,bootstyle="success", text="Agregar Producto", command=self.ventana_agregar_producto)
			btn_agregar.grid(row=1, column=0, padx=10, pady=10)

			btn_actualizar = tb.Button(self.frame_lista_producto,bootstyle="warning", text="Actualizar Producto", command=self.actualizar_producto)
			btn_actualizar.grid(row=1, column=1, padx=10, pady=10)

			btn_eliminar = tb.Button(self.frame_lista_producto,bootstyle="danger", text="Eliminar Producto", command=self.eliminar_producto)
			btn_eliminar.grid(row=1, column=2, padx=10, pady=10)

			# Llamamos a nuestra función para mostrar productos
			self.mostrar_productos()

		def mostrar_productos(self):
			try:
					conexion = sqlite3.connect("sistema.db")
					cur = conexion.cursor()
					registros = self.tree_lista_productos.get_children()
					for e in registros:
							self.tree_lista_productos.delete(e)

					cur.execute("SELECT * FROM productos ORDER BY codigo DESC;")
					datos = cur.fetchall()
					for row in datos:
							self.tree_lista_productos.insert("", "end", values=row)

					conexion.commit()
			except sqlite3.Error as e:
					messagebox.showerror("Lista de Productos", f"Ocurrió un error al mostrar los productos: {e}")
			finally:
					conexion.close()

		def ventana_agregar_producto(self):
				self.ventana_producto = tk.Toplevel(self)
				self.ventana_producto.title("Agregar Producto")
				self.ventana_producto.geometry("300x500")

				# Entradas para los detalles del producto
				tk.Label(self.ventana_producto, text="Código").pack(pady=5)
				self.txt_codigo = ttk.Entry(self.ventana_producto)
				self.txt_codigo.pack(pady=5)

				tk.Label(self.ventana_producto, text="Nombre").pack(pady=5)
				self.txt_nombre = ttk.Entry(self.ventana_producto)
				self.txt_nombre.pack(pady=5)

				tk.Label(self.ventana_producto, text="Stock").pack(pady=5)
				self.txt_stock = ttk.Entry(self.ventana_producto)
				self.txt_stock.pack(pady=5)

				tk.Label(self.ventana_producto, text="Precio").pack(pady=5)
				self.txt_precio = ttk.Entry(self.ventana_producto)
				self.txt_precio.pack(pady=5)

				tk.Label(self.ventana_producto, text="Origen").pack(pady=5)
				self.txt_origen = ttk.Entry(self.ventana_producto)
				self.txt_origen.pack(pady=5)

				tk.Label(self.ventana_producto, text="Tipo de Producto").pack(pady=5)
				self.txt_tipo = ttk.Entry(self.ventana_producto)
				self.txt_tipo.pack(pady=5)
			
				btn_guardar = tb.Button(self.ventana_producto, text="Guardar", command=self.guardar_producto)
				btn_guardar.pack(pady=10)

		def guardar_producto(self):
				try:
						conexion = sqlite3.connect("sistema.db")
						cur = conexion.cursor()
						cur.execute("INSERT INTO productos (codigo, nombre, stock, precio, origen, tipo_producto) VALUES (?, ?, ?, ?, ?, ?)",
						(self.txt_codigo.get(), self.txt_nombre.get(), self.txt_stock.get(), self.txt_precio.get(), self.txt_origen.get(), self.txt_tipo.get()))
						conexion.commit()
						self.mostrar_productos()
						self.ventana_producto.destroy()  # Cerrar la ventana después de guardar
				except sqlite3.Error as e:
					messagebox.showerror("Agregar Producto", f"Ocurrió un error al agregar el producto: {e}")
				finally:
					conexion.close()

		def actualizar_producto(self):
					selected_item = self.tree_lista_productos.selection()
					if not selected_item:
							messagebox.showwarning("Actualizar Producto", "Por favor, selecciona un producto para actualizar.")
							return

					item_values = self.tree_lista_productos.item(selected_item, 'values')
					self.ventana_producto = tk.Toplevel(self)
					self.ventana_producto.title("Actualizar Producto")
					self.ventana_producto.geometry("300x500")

					# Entradas para los detalles del producto
					tk.Label(self.ventana_producto, text="Código").pack(pady=5)
					self.txt_codigo = ttk.Entry(self.ventana_producto)
					self.txt_codigo.pack(pady=5)
					self.txt_codigo.insert(0, item_values[0])  # Código

					tk.Label(self.ventana_producto, text="Nombre").pack(pady=5)
					self.txt_nombre = ttk.Entry(self.ventana_producto)
					self.txt_nombre.pack(pady=5)
					self.txt_nombre.insert(0, item_values[1])  # Nombre

					tk.Label(self.ventana_producto, text="Stock").pack(pady=5)
					self.txt_stock = ttk.Entry(self.ventana_producto)
					self.txt_stock.pack(pady=5)
					self.txt_stock.insert(0, item_values[2])  # Stock

					tk.Label(self.ventana_producto, text="Precio").pack(pady=5)
					self.txt_precio = ttk.Entry(self.ventana_producto)
					self.txt_precio.pack(pady=5)
					self.txt_precio.insert(0, item_values[3])  # Precio

					tk.Label(self.ventana_producto, text="Origen").pack(pady=5)
					self.txt_origen = ttk.Entry(self.ventana_producto)
					self.txt_origen.pack(pady=5)
					self.txt_origen.insert(0, item_values[4])  # Origen

					tk.Label(self.ventana_producto, text="Tipo de Producto").pack(pady=5)
					self.txt_tipo = ttk.Entry(self.ventana_producto)
					self.txt_tipo.pack(pady=5)
					self.txt_tipo.insert(0, item_values[5])  # Tipo de Producto

					btn_guardar = tb.Button(self.ventana_producto, text="Actualizar", command=lambda: self.guardar_actualizacion(item_values[0]))
					btn_guardar.pack(pady=10)

		def guardar_actualizacion(self, codigo):
				try:
						conexion = sqlite3.connect("sistema.db")
						cur = conexion.cursor()
						cur.execute("UPDATE productos SET nombre=?, stock=?, precio=?, origen=?, tipo_producto=? WHERE codigo=?",
												(self.txt_nombre.get(), self.txt_stock.get(), self.txt_precio.get(), self.txt_origen.get(), self.txt_tipo.get(), codigo))
						conexion.commit()
						self.mostrar_productos()
						self.ventana_producto.destroy()  # Cerrar la ventana después de actualizar
				except sqlite3.Error as e:
						messagebox.showerror("Actualizar Producto", f"Ocurrió un error al actualizar el producto: {e}")
				finally:
						conexion.close()

		def eliminar_producto(self):
					selected_item = self.tree_lista_productos.selection()
					if not selected_item:
							messagebox.showwarning("Eliminar Producto", "Por favor, selecciona un producto para eliminar.")
							return

					item_values = self.tree_lista_productos.item(selected_item, 'values')
					confirm = messagebox.askyesno("Eliminar Producto", f"¿Estás seguro de que deseas eliminar el producto '{item_values[1]}'?")
					if confirm:
							try:
										conexion = sqlite3.connect("sistema.db")
										cur = conexion.cursor()
										cur.execute("DELETE FROM productos WHERE codigo=?", (item_values[0],))
										conexion.commit()
										self.mostrar_productos()  # Actualizar la lista de productos
										messagebox.showinfo("Eliminar Producto", "Producto eliminado con éxito.")
							except sqlite3.Error as e:
										messagebox.showerror("Eliminar Producto", f"Ocurrió un error al eliminar el producto: {e}")
							finally:
										conexion.close()	

def open_vista_producto(root):
		vista_cliente = tk.Toplevel(root)
		vista_cliente.title('Productos')
		vista_cliente.resizable(0, 0)

		app = Frame3(vista_cliente)  
		



				


