# ITec-Backtend

## Práctico 4: SQLModel y Alembic

Aprendimos a usar SQLAlchemy, ahora lo reemplazamos con SQLModel para unificar nuestros Schemas con nuestros Models. Además, usamos Alembic para crear migraciones de DB y registrar los cambios de la estructura de la base de datos.

### Para este práctico:

- Reemplazar el SQLAlchemy funcional por SQLModel; adaptando tanto la database.py como models.py.
- Inicializar Alembic, donde exista por lo menos una migración inicial que se encargue de levantar (crear) la DB.
- Agregar otro modelo (tabla) que guarde algún tipo de relación (clave foránea) con la existente.
