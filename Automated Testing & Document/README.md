# Automatización de login en SauceDemo con Selenium

Aqui encontraras el proceso de Automatización del login en [SauceDemo](https://www.saucedemo.com/) utilizando **Python + Selenium**.  
Objetivo: realizar inicio de sesión y validar el resultado en base a una matriz de prueba.

---

## Requisitos
- Python 3.8 o superior  
- Librería Selenium instalada (`pip install selenium`)  
- Google Chrome actualizado (versión 148 o superior)  
- ChromeDriver compatible con tu versión de Chrome, ubicado en `C:/drivers/chromedriver.exe`  

---

## Ejecución
1. Clona este repositorio o descarga los archivos.  
2. Verifica tener `chromedriver.exe` en la carpeta `C:/drivers/`.  
3. Ejecuta el script principal desde la terminal:  
   ```bash
   python automatización.py

## Resultados esperados
1. El navegador abre la página de SauceDemo.

2. Se llenan automáticamente los campos de usuario y contraseña.

3. Se hace clic en el botón de login.

4. El título de la página cambia a: Swag Labs.

## Matriz de prueba
Se encuentra en el archivo [MatrizPrueba-Saucedemo.xlsx](MatrizPrueba-Saucedemo.xlsx).

## Evidencia de prueba
Se encuentra en el archivo [evidencia-automatización.docx](evidencia-automatización.docx).
