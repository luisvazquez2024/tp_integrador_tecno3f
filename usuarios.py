from tkinter import *;
from tkinter import ttk,messagebox;
from productos import open_vista_producto
import ttkbootstrap as tb;
import sqlite3;



class Ventana(tb.Window):
		def __init__(self):
				super().__init__();
				self.ventana_login()
				
  
  		
		def ventana_login(self):

			self.frame_login=Frame(self)
			self.frame_login.pack()
			
			self.lblframe_login=LabelFrame(self.frame_login,text="Acceso");
			self.lblframe_login.pack(padx=10,pady=10);
			
			self.lbltitulo=Label(self.lblframe_login,text="Inicio de sesión", font=('Arial',20,'bold'))
			self.lbltitulo.pack(padx=10, pady=35)
			
   
			self.txt_usuario=ttk.Entry(self.lblframe_login, width=40, justify=CENTER);
			self.txt_usuario.pack(padx=10,pady=10);
			self.txt_clave=ttk.Entry(self.lblframe_login, width=40, justify=CENTER);
			self.txt_clave.pack(padx=10,pady=10);
			self.txt_clave.configure(show="*")
			self.btn_acceso=ttk.Button(self.lblframe_login, text="Log in",width=38,command=self.logueo);
			self.btn_acceso.pack(padx=10,pady=10);	
   
		def ventana_menu(self): 
				self.frame_left=Frame(self, width=200);
				self.frame_left.grid(row=0, column=0,sticky=NSEW);
				self.frame_center=Frame(self);
				self.frame_center.grid(row=0, column=1,sticky=NSEW);
				self.frame_rigth=Frame(self, width=400);
				self.frame_rigth.grid(row=0, column=2,sticky=NSEW);
    
				btn_productos=ttk.Button(self.frame_left, text="Productos",width=15, command=lambda: open_vista_producto(self))
				btn_productos.grid(row=1, column=0,padx=10, pady=10)		
				btn_clientes=ttk.Button(self.frame_left, text="Clientes",width=15)
				btn_clientes.grid(row=3, column=0,padx=10, pady=10)		
				btn_usuarios=ttk.Button(self.frame_left, text="Usuarios",width=15, command=self.ventana_lista_usuario)
				btn_usuarios.grid(row=5, column=0,padx=10, pady=10)		
				btn_reportes=ttk.Button(self.frame_left, text="Reportes",width=15)
				btn_reportes.grid(row=6, column=0,padx=10, pady=10)		
				btn_salir=ttk.Button(self.frame_left, text="Salir",width=15, command=self.destroy)
				btn_salir.grid(row=8, column=0,padx=10, pady=10)	
    	
		def logueo(self):
			try:
					# establace la conexion con la BD
					conexion=sqlite3.connect("sistema.db");
					#creamos el cursor
					cur = conexion.cursor();
					
					nombre_usuario=self.txt_usuario.get();
					clave_usuario=self.txt_clave.get();
     
					#consultamos nuestra base de datos
					cur.execute("SELECT * FROM usuarios WHERE nombre=? AND clave=?",(nombre_usuario,clave_usuario))
					#con esto traemos todos los registros y lo guardamos en 'datos'
					datos_logueo=cur.fetchall();
					if datos_logueo:
								row=datos_logueo[0]
								cod_usu=row[0]
								nom_usu=row[1]
								clav_usu=row[2]
								rol_usu=row[3]
								if(nom_usu == self.txt_usuario.get() and clav_usu == self.txt_clave.get()):
									self.frame_login.pack_forget() # con esta linea ocultamos la ventana login
									self.ventana_menu(); #con esta lina abrimos la ventana menu	
					else:
							messagebox.showerror("Acceso", "El usuario o clave son incorrectos!")				
					#aplicamos cambios
					conexion.commit()
			except sqlite3.Error as e:
				messagebox.showerror("Lista de Usuario", f"Ocurrió un error al mostrar los usuarios: {e}")
			finally:
				#cerramos la conexion independiente del resultado
				conexion.close()
		def ventana_lista_usuario(self):
			self.frame_lista_usuario=Frame(self.frame_center);
			self.frame_lista_usuario.grid(row=0,column=0,padx=10,pady=10,columnspan=2,sticky=NSEW)
			
			self.lblfframe_botones_listusu =LabelFrame(self.frame_lista_usuario);
			self.lblfframe_botones_listusu.grid(row=0,column=0,padx=5,pady=5,sticky=NSEW)
   
			btn_nuevo_usuario = tb.Button(self.lblfframe_botones_listusu,text="Nuevo",width=15,bootstyle="success",command=self.ventana_nuevo_usuario)
			btn_nuevo_usuario.grid(row=0,column=0,padx=10,pady=10)

			btn_modificar_usuario = tb.Button(self.lblfframe_botones_listusu,text="Modificar",width=15,bootstyle="warning", command=self.ventana_modificar_usuarios)
			btn_modificar_usuario.grid(row=0,column=1,padx=10,pady=10)

			btn_eliminar_usuario = tb.Button(self.lblfframe_botones_listusu,text="Eliminar",width=15,bootstyle="danger", command=self.eliminar_usuario)
			btn_eliminar_usuario.grid(row=0,column=2,padx=10,pady=10)
			
			self.lblfframe_busqueda_listusu =LabelFrame(self.frame_lista_usuario);
			self.lblfframe_busqueda_listusu.grid(row=1,column=0,padx=10,pady=10,sticky=NSEW);
   
			self.txt_busqueda_usuarios=ttk.Entry(self.lblfframe_busqueda_listusu,width=95);
			self.txt_busqueda_usuarios.grid(row=0,column=0,padx=10,pady=10)
			self.bind('<Key>',self.busqueda_usuario)
   
   #============================Treeview===================================#
   		
			self.lblfframe_tree_listusu =LabelFrame(self.frame_lista_usuario);
			self.lblfframe_tree_listusu.grid(row=2,column=0,sticky=NSEW)
   
   
			columnas = ("codigo", "nombre", "clave","rol");
   
			self.tree_lista_usuarios=tb.Treeview(self.lblfframe_tree_listusu,columns=columnas, height=17, show="headings",bootstyle="dark");
			self.tree_lista_usuarios.grid(row=0,column=0);
   
			self.tree_lista_usuarios.heading("codigo",text="Codigo", anchor=W)
			self.tree_lista_usuarios.heading("nombre",text="Nombre", anchor=W)
			self.tree_lista_usuarios.heading("clave",text="Clave", anchor=W)
			self.tree_lista_usuarios.heading("rol",text="Rol", anchor=W)
			self.tree_lista_usuarios['displaycolumns']=("codigo","nombre","rol")#oculta la clave solo aparece nombre y rol

			##Crear el scrollbar
   
			tree_scroll_listausu=tb.Scrollbar(self.frame_lista_usuario,bootstyle="round-success");
			tree_scroll_listausu.grid(row=2,column=1);
   #configurar el scrollbar
			tree_scroll_listausu.config(command=self.tree_lista_usuarios.yview)
   # Llamamos a nuestra funcion mostrar usuarios
			self.mostrar_usuarios();
		def mostrar_usuarios(self):
			try:
				# establace la conexion con la BD
				conexion=sqlite3.connect("sistema.db");
				#creamos el cursor
				cur = conexion.cursor();
				#limpiamos nuestro treeview
				registros=self.tree_lista_usuarios.get_children();
				#recorremos cada registro
				for e in registros:
					self.tree_lista_usuarios.delete(e)
				#consultamos nuestra base de datos
				cur.execute("SELECT * FROM usuarios ORDER BY id DESC;")
				#con esto traemos todos los registros y lo guardamos en 'datos'
				datos=cur.fetchall();
				#recorremos cada fila encontrada
				for row in datos:
						#llenamos nuestro treeview
						self.tree_lista_usuarios.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]));
				#aplicamos cambios
				conexion.commit()
			except sqlite3.Error as e:
				messagebox.showerror("Lista de Usuario", f"Ocurrió un error al mostrar los usuarios: {e}")
			finally:
				#cerramos la conexion independiente del resultado
				conexion.close()
		def ventana_nuevo_usuario(self):
			self.frame_nuevo_usuario=Toplevel(self);
			self.frame_nuevo_usuario.title("Nuevo Usuario"); #Titulo de la nueva ventana para el nuevo usuario
			self.centrar_ventana_nuevo_usuario(400,300); #tamanio de la ventana
			self.frame_nuevo_usuario.resizable(0,0);#para que no se pueda max ni minimizar la ventana
			self.frame_nuevo_usuario.grab_set();#para que no permita ninguna otra accion hasta que se cierre la ventana
			
			lblframe_nuevo_usuario=LabelFrame(self.frame_nuevo_usuario)
			lblframe_nuevo_usuario.grid(row=0, column=0, padx=10, pady=10,sticky=NSEW)
   
			lbl_codigo_nuevo_usuario=ttk.Label(lblframe_nuevo_usuario, text="Codigo")
			lbl_codigo_nuevo_usuario.grid(row=0, column=0, padx=10, pady=10,sticky=NSEW)
			self.txt_codigo_nuevo_usuario=ttk.Entry(lblframe_nuevo_usuario, width=40)
			self.txt_codigo_nuevo_usuario.grid(row=0, column=1, padx=10, pady=10,sticky=NSEW)
   
			lbl_nombre_nuevo_usuario=ttk.Label(lblframe_nuevo_usuario, text="Nombre")
			lbl_nombre_nuevo_usuario.grid(row=1, column=0, padx=10, pady=10,sticky=NSEW)
			self.txt_nombre_nuevo_usuario=ttk.Entry(lblframe_nuevo_usuario, width=40)
			self.txt_nombre_nuevo_usuario.grid(row=1, column=1, padx=10, pady=10,sticky=NSEW)
   
			lbl_clave_nuevo_usuario=ttk.Label(lblframe_nuevo_usuario, text="Clave")
			lbl_clave_nuevo_usuario.grid(row=2, column=0, padx=10, pady=10,sticky=NSEW)
			self.txt_clave_nuevo_usuario=ttk.Entry(lblframe_nuevo_usuario, width=40)
			self.txt_clave_nuevo_usuario.grid(row=2, column=1, padx=10, pady=10,sticky=NSEW)
   
			lbl_rol_nuevo_usuario=Label(lblframe_nuevo_usuario, text="Rol")
			lbl_rol_nuevo_usuario.grid(row=3, column=0, padx=10, pady=10,sticky=NSEW)
			self.txt_rol_nuevo_usuario=ttk.Combobox(lblframe_nuevo_usuario,values=('admin','empleado','cliente') ,width=40, state="readonly")
			self.txt_rol_nuevo_usuario.grid(row=3, column=1, padx=10, pady=10,sticky=NSEW)
			self.txt_rol_nuevo_usuario.current(0);		
   
			btn_guardar_nuevo_usuario=ttk.Button(lblframe_nuevo_usuario, text="Guardar",width=40, command=self.guardar_usuario)
			btn_guardar_nuevo_usuario.grid(row=4,column=1, padx=10, pady=10)
			
			#llamamos a la funcion ultimo usuario
			self.ultimo_usuario();
			self.txt_nombre_nuevo_usuario.focus();
		def guardar_usuario(self):
				if (self.txt_codigo_nuevo_usuario.get()=="" or self.txt_nombre_nuevo_usuario.get()=="" or
				self.txt_clave_nuevo_usuario.get() == ""):
					messagebox.showwarning("guardando usuario", "Algun campo no es valido por favor revise")
					return
    
				try:
					
					# establace la conexion con la BD
					conexion=sqlite3.connect("sistema.db");
					#creamos el cursor
					cur = conexion.cursor();
					
					datos_guardar_usuario=self.txt_codigo_nuevo_usuario.get(),self.txt_nombre_nuevo_usuario.get(),self.txt_clave_nuevo_usuario.get(),self.txt_rol_nuevo_usuario.get()	
     
					#consultamos nuestra base de datos
					cur.execute("INSERT INTO usuarios VALUES(?,?,?,?)",(datos_guardar_usuario))
					messagebox.showinfo("Guardando usuario...", "usuario guardado correctamente");
							
					#aplicamos cambios
					conexion.commit()
				except sqlite3.Error as e:
						conexion.rollback();
						messagebox.showerror("Guardando usuario...", f"Ocurrió un error al guardar los usuarios: {e}")
				finally:
					self.frame_nuevo_usuario.destroy()#cerramos la ventana al guardar el nuevo usuario
					self.ventana_lista_usuario()#cargamos nuevamente la lista de usuarios
					#cerramos la conexion independiente del resultado
					conexion.close()
		def ultimo_usuario(self):
					try:
							# establace la conexion con la BD
							conexion=sqlite3.connect("sistema.db");
							#creamos el cursor
							cur = conexion.cursor();
							#consultamos nuestra base de datos
							cur.execute("SELECT MAX(id) FROM usuarios;");
							datos=cur.fetchone()#solo necesitamos uno solo
							for codusu in datos:
								if codusu==None:
										self.ultusu=(int(1))
										self.txt_codigo_nuevo_usuario.config(state=NORMAL)
										self.txt_codigo_nuevo_usuario.insert(0,self.ultusu)
										self.txt_codigo_nuevo_usuario.config(state="readonly")
										
								if codusu=="":
										self.ultusu=(int(1))
										self.txt_codigo_nuevo_usuario.config(state=NORMAL)
										self.txt_codigo_nuevo_usuario.insert(0,self.ultusu)
										self.txt_codigo_nuevo_usuario.config(state="readonly")
										
								else:
										self.ultusu=(int(codusu)+1)
										self.txt_codigo_nuevo_usuario.config(state=NORMAL)
										self.txt_codigo_nuevo_usuario.insert(0,self.ultusu)
										self.txt_codigo_nuevo_usuario.config(state="readonly")	
					except sqlite3.Error as e:
								messagebox.showerror("Lista Usuario", f"Ocurrió un error al intentar obtener el codigo usuario: {e}")
					finally:
								#cerramos la conexion independiente del resultado
								conexion.close()
		def centrar_ventana_nuevo_usuario(self, ancho,alto):
				ventana_ancho=ancho;
				ventana_alto=alto;
				pantalla_ancho=self.frame_rigth.winfo_screenwidth()
				pantalla_alto=self.frame_rigth.winfo_screenheight()
				coordenadas_x=int((pantalla_ancho/2)-(ventana_ancho/2))
				coordenadas_y=int((pantalla_alto/2)-(ventana_alto/2))
				self.frame_nuevo_usuario.geometry(f"{ventana_ancho}x{ventana_alto}+{coordenadas_x}+{coordenadas_y}")				
		def busqueda_usuario(self,event):
				try:
						
						# establace la conexion con la BD
						conexion=sqlite3.connect("sistema.db");
      			#creamos el cursor
						cur = conexion.cursor();
						#limpiamos nuestro treeview
						registros=self.tree_lista_usuarios.get_children();
						#recorremos cada registro
						for e in registros:
							self.tree_lista_usuarios.delete(e)
						#consultamos nuestra base de datos
						cur.execute("SELECT * FROM usuarios WHERE nombre LIKE ?;",(self.txt_busqueda_usuarios.get()+'%',))
						#con esto traemos todos los registros y lo guardamos en 'datos'
						datos=cur.fetchall();
						#recorremos cada fila encontrada
						for row in datos:
								#llenamos nuestro treeview
								self.tree_lista_usuarios.insert("",0,text=row[0],values=(row[0],row[1],row[2],row[3]));
						#aplicamos cambios
						conexion.commit()
				except sqlite3.Error as e:	
					messagebox.showerror("Busqueda Usuario", f"Ocurrió un error al buscar el usuario: {e}")
				finally:
					#cerramos la conexion independiente del resultado
					conexion.close()
		def ventana_modificar_usuarios(self):
				#con esto validamos que se abra la venta solo si hay algun valor selccionado.
			self.usuario_seleccionado=self.tree_lista_usuarios.focus();
			self.val_mod_usu=self.tree_lista_usuarios.item(self.usuario_seleccionado,"values");
		
			if self.val_mod_usu!='':
				self.frame_modificar_usuario=Toplevel(self);
				self.frame_modificar_usuario.title("Modificar Usuario"); #Titulo de la nueva ventana para el nuevo usuario
				self.frame_modificar_usuario.geometry("400x300");		
				#self.centrar_ventana_nuevo_usuario(400,300); #tamanio de la ventana
				self.frame_modificar_usuario.resizable(0,0);#para que no se pueda max ni minimizar la ventana
				self.frame_modificar_usuario.grab_set();#para que no permita ninguna otra accion hasta que se cierre la ventana
				
				lblframe_modificar_usuario=LabelFrame(self.frame_modificar_usuario)
				lblframe_modificar_usuario.grid(row=0, column=0, padx=10, pady=10,sticky=NSEW)
		
				lbl_codigo_modificar_usuario=ttk.Label(lblframe_modificar_usuario, text="Codigo")
				lbl_codigo_modificar_usuario.grid(row=0, column=0, padx=10, pady=10,sticky=NSEW)
				self.txt_codigo_modificar_usuario=ttk.Entry(lblframe_modificar_usuario, width=40)
				self.txt_codigo_modificar_usuario.grid(row=0, column=1, padx=10, pady=10,sticky=NSEW)
		
				lbl_nombre_modificar_usuario=ttk.Label(lblframe_modificar_usuario, text="Nombre")
				lbl_nombre_modificar_usuario.grid(row=1, column=0, padx=10, pady=10,sticky=NSEW)
				self.txt_nombre_modificar_usuario=ttk.Entry(lblframe_modificar_usuario, width=40)
				self.txt_nombre_modificar_usuario.grid(row=1, column=1, padx=10, pady=10,sticky=NSEW)
		
				lbl_clave_modificar_usuario=ttk.Label(lblframe_modificar_usuario, text="Clave")
				lbl_clave_modificar_usuario.grid(row=2, column=0, padx=10, pady=10,sticky=NSEW)
				self.txt_clave_modificar_usuario=ttk.Entry(lblframe_modificar_usuario, width=40)
				self.txt_clave_modificar_usuario.grid(row=2, column=1, padx=10, pady=10,sticky=NSEW)
		
				lbl_rol_modificar_usuario=Label(lblframe_modificar_usuario, text="Rol")
				lbl_rol_modificar_usuario.grid(row=3, column=0, padx=10, pady=10,sticky=NSEW)
				self.txt_rol_modificar_usuario=ttk.Combobox(lblframe_modificar_usuario,values=('admin','empleado','cliente') ,width=40)
				self.txt_rol_modificar_usuario.grid(row=3, column=1, padx=10, pady=10,sticky=NSEW)
			
		
				btn_guardar_modificar_usuario=tb.Button(lblframe_modificar_usuario, text="Modificar",width=40, command=self.modificar_usuario, bootstyle="warning")
				btn_guardar_modificar_usuario.grid(row=4,column=1, padx=10, pady=10)
				self.llenar_entry_modificar_usuarios();
				self.txt_nombre_modificar_usuario.focus()
    
		def llenar_entry_modificar_usuarios(self):
				#limpiamos los entryes
				self.txt_codigo_modificar_usuario.delete(0,END)
				self.txt_nombre_modificar_usuario.delete(0,END)
				self.txt_clave_modificar_usuario.delete(0,END)
				self.txt_rol_modificar_usuario.delete(0,END)
				#Llenamos los entries
				self.txt_codigo_modificar_usuario.insert(0,self.val_mod_usu[0])
				self.txt_codigo_modificar_usuario.config(state='readonly')
				self.txt_nombre_modificar_usuario.insert(0,self.val_mod_usu[1])
				self.txt_clave_modificar_usuario.insert(0,self.val_mod_usu[2])
				self.txt_rol_modificar_usuario.insert(0,self.val_mod_usu[3])
				self.txt_rol_modificar_usuario.config(state='readonly')	
		def modificar_usuario(self):          
				if (self.txt_codigo_modificar_usuario.get()=="" or self.txt_nombre_modificar_usuario.get()=="" or
				self.txt_clave_modificar_usuario.get() == ""):
						messagebox.showwarning("guardando usuario", "Algun campo no es valido por favor revise")
						return

				try:
						
						# establace la conexion con la BD
						conexion=sqlite3.connect("sistema.db");
						#creamos el cursor
						cur = conexion.cursor();
						
						datos_modificar_usuario=self.txt_nombre_modificar_usuario.get(),self.txt_clave_modificar_usuario.get(),self.txt_rol_modificar_usuario.get()	

						#consultamos nuestra base de datos
						cur.execute("UPDATE usuarios SET nombre=?,clave=?,rol=? WHERE id= "+self.txt_codigo_modificar_usuario.get(),(datos_modificar_usuario))
						messagebox.showinfo("Modificando usuario...", "usuario Modificado correctamente");
								
						#aplicamos cambios
						conexion.commit()
						self.val_mod_usu=self.tree_lista_usuarios.item(self.usuario_seleccionado,text='',values=(self.txt_codigo_modificar_usuario.get(),self.txt_nombre_modificar_usuario.get(),self.txt_clave_modificar_usuario.get(),self.txt_rol_modificar_usuario.get(),))
				except sqlite3.Error as e:
							messagebox.showerror("Modificando usuario...", f"Ocurrió un error al Modificar el usuario: {e}")
				finally:
						
						self.frame_modificar_usuario.destroy()#cerramos la ventana al guardar el nuevo usuario
						#self.ventana_lista_usuario()#cargamos nuevamente la lista de usuarios
						#cerramos la conexion independiente del resultado
						conexion.close()

		def delete_user(self,user_id):
				try:
						print("Conectando a la base de datos...")
						conexion = sqlite3.connect("sistema.db")
						cur = conexion.cursor()
						print(f"Ejecutando consulta para eliminar el usuario con ID: {user_id}")
						cur.execute("DELETE FROM usuarios WHERE id=?", (user_id,))
						conexion.commit()
						
						print(f"Filas afectadas: {cur.rowcount}")
						if cur.rowcount > 0:
								messagebox.showinfo("Eliminando usuario...", "Usuario eliminado correctamente")
						else:
								messagebox.showwarning("Eliminando usuario...", "No se encontró un usuario con ese ID")
				except sqlite3.Error as e:
						print(f"Error al eliminar el usuario: {e}")
						messagebox.showerror("Eliminando usuario...", f"Ocurrió un error al eliminar el usuario: {e}")
						conexion.rollback()
				finally:
						conexion.close()				
		def eliminar_usuario(self):
						usuario_seleccionado = self.tree_lista_usuarios.focus()
						if not usuario_seleccionado:
								messagebox.showwarning("Eliminar Usuario", "Por favor, selecciona un usuario para eliminar.")
								return

						user_id = self.tree_lista_usuarios.item(usuario_seleccionado, "values")[0]  # Asumiendo que el ID es el primer valor
						confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que deseas eliminar el usuario con ID {user_id}?")
						if confirmacion:
									self.delete_user(user_id)  # Llamada a la función independiente
									self.mostrar_usuarios()  # Actualiza la lista de usuarios después de eliminar
				