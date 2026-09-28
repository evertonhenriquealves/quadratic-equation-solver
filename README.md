# 🧮 Quadratic Equation Solver (Bhaskara CLI)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)

> 🇬🇧 A Python CLI application that solves quadratic equations ($ax^2 + bx + c = 0$) using custom exception handling (`ValueError`, `ArithmeticError`) for zero-coefficient and negative discriminant ($\Delta < 0$) validation.  
>  
> 🇧🇷 Uma aplicação CLI em Python que resolve equações do segundo grau ($ax^2 + bx + c = 0$) com tratamento customizado de exceções (`ValueError`, `ArithmeticError`) para coeficientes nulos e deltas negativos ($\Delta < 0$).

---

## ⚙️ Features / Funcionalidades

* **Bhaskara Formula Engine:** Computes real roots ($x_1, x_2$) for quadratic equations.
* **Custom Exception Handling:**
  * Lança `ValueError` caso o coeficiente $a = 0$ (não caracterizando equação de 2º grau).
  * Lança `ArithmeticError` caso o discriminante $\Delta < 0$ (sem raízes reais).
* **Interactive CLI Loop:** Allows continuous calculations with screen clearing and exit options.

---

## 🛠️ How to Run / Como Executar

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/evertonhenriquealves/quadratic-equation-solver.git](https://github.com/evertonhenriquealves/quadratic-equation-solver.git)
   cd quadratic-equation-solver