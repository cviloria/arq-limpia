# Shopping Cart Application

Esta es una aplicación simple de carrito de compras utilizando Flask y siguiendo la Clean Architecture.

## Estructura del Proyecto


Claro, a continuación te dejo un archivo README.md que te guiará para inicializar y ejecutar el proyecto:

markdown
Copiar código
# Shopping Cart Application

Esta es una aplicación simple de carrito de compras utilizando Flask y siguiendo la Clean Architecture.

## Estructura del Proyecto
```
shopping_cart/
|-- app/
| |-- init.py
| |-- main.py
|-- core/
| |-- init.py
| |-- domain/
| | |-- init.py
| | |-- models.py
| |-- use_cases/
| |-- init.py
| |-- cart_use_cases.py
|-- interfaces/
| |-- init.py
| |-- api/
| | |-- init.py
| | |-- cart_controller.py
|-- requirements.txt
|-- run.py
```

## Requisitos Previos

- Python 3.7 o superior
- `pip` (el gestor de paquetes de Python)

## Instalación

1. **Clonar el repositorio**:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd practica-4
    ```

2. **Crear y activar un entorno virtual**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Instalar las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

## Ejecución de la Aplicación

1. **Inicializar la aplicación Flask**:

    ```bash
    python run.py
    ```

2. **Acceder a la aplicación**:

    Abre tu navegador y navega a `http://127.0.0.1:5000/`

## Rutas Disponibles

- **POST /cart**: Añade un producto al carrito.
  - Cuerpo de la solicitud (JSON):
    ```json
    {
        "product_id": 1,
        "name": "Product 1",
        "price": 10.0,
        "quantity": 2
    }
    ```

- **DELETE /cart/<int:product_id>**: Elimina un producto del carrito por ID.

- **GET /cart/total**: Obtiene el total del carrito.

## Ejemplos de Uso

### Añadir un producto al carrito

```bash
curl -X POST http://127.0.0.1:5000/cart -H "Content-Type: application/json" -d '{
    "product_id": 1,
    "name": "Product 1",
    "price": 10.0,
    "quantity": 2
}'

### Eliminar un producto del carrito
```bash
curl -X DELETE http://127.0.0.1:5000/cart/1
```
###Obtener el total del carrito
```bash
curl http://127.0.0.1:5000/cart/total
```

### Estructura del Código
Dominio
Define los modelos de dominio como Product, CartItem y Cart en core/domain/models.py.

### Casos de Uso
Implementa la lógica del negocio en core/use_cases/cart_use_cases.py.

### Controlador de API
Define los controladores de la API para manejar las solicitudes HTTP en interfaces/api/cart_controller.py.

### Aplicación Principal
Configura y ejecuta la aplicación Flask en app/main.py.

### Ejecución
El archivo run.py se utiliza para iniciar la aplicación Flask.


### Ejecutar pruebas
```bash
pytest --cov-config=.coveragerc --cov --cov-report=html --html=htmlcov/report.html
```

