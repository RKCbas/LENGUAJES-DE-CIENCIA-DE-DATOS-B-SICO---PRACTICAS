from InquirerPy import inquirer
from rich.console import Console

console = Console()

def sumar(a, b): 
    return a + b
def restar(a, b): 
    return a - b
def multiplicar(a, b): 
    return a * b
def dividir(a, b): 
    if b != 0:
        return a / b
    else:
        raise ValueError("Error de división entre 0")

while(True):
    try:
        console.print("[bold cyan]=== Calculadora Básica ===[/bold cyan]")
        
        operación = inquirer.select(
            message="Elige una operación:",
            choices=["Sumar", "Restar", "Multiplicar", "Dividir", "Salir"],
        ).execute()

        if operación == "Salir":
            console.print("[bold red]Saliendo...[/bold red]")
            break

        a = float(inquirer.text(message="Ingresa el primer número:").execute())
        b = float(inquirer.text(message="Ingresa el segundo número:").execute())

        # Calcular resultado
        resultado = {
            "Sumar": sumar,
            "Restar": restar,
            "Multiplicar": multiplicar,
            "Dividir": dividir,
        }[operación](a, b)

        console.print(f"\n[bold green]Resultado de {operación} {a} y {b}: [yellow]{resultado}[/yellow]\n")

    except ValueError as e:
        console.print(f"[bold red]{e}[/bold red]")
        break
    except TypeError:
        console.print("[bold red]Ingrese un valor valido...[/bold red]")