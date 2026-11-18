# Lab 12 - Django: Formularios, Admin, Middleware y Autenticación

Práctica de Desarrollo de Aplicaciones Web (IS093A), UNCP.
Autora: Jackeline Vivanco Solano.

## Qué incluye
- **Fase 1:** modelo `Producto`, `ModelForm` y formulario clásico, plantilla con CSRF.
- **Fase 2:** validación en 3 niveles (regex, `clean_<campo>()`, `clean()`) y `sanitize_input()`.
- **Fase 3:** Django Admin con filtros, búsqueda, campo calculado y acción masiva.
- **Fase 4:** middleware de auditoría, sesiones, login/logout/registro, `@login_required` y permisos.
- **Fase 5:** `check --deploy` y auditoría (`AUDITORIA.txt`).

## Cómo ejecutarlo
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Rutas
| Ruta | Descripción |
| --- | --- |
| `/` | Lista de productos (requiere permiso `view_producto`) |
| `/producto/nuevo/` | Crear producto (requiere login) |
| `/registro/` | Registro de usuarios |
| `/accounts/login/` | Inicio de sesión |
| `/admin/` | Panel de administración |

## Uso de IA
Se usó Claude como asistente para guiar y depurar. Los problemas resueltos están documentados en el informe.