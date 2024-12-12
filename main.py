from usuarios import Ventana,barrita_menu;
import ttkbootstrap as tb;

def main():
		app=Ventana();
		app.title("Sistema de Inventario");
		app.state("zoomed");
		barrita_menu(app)
		tb.Style('superhero')
		app.mainloop()


if __name__=='__main__':
		main()  