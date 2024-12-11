from usuarios import Ventana;
import ttkbootstrap as tb;

def main():
		app=Ventana();
		app.title("Sistema de Inventario");
		app.state("zoomed");
		tb.Style('superhero')
		app.mainloop()


if __name__=='__main__':
		main()  