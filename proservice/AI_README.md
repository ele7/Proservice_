# Integración con Claude Haiku 4.5 (Anthropic)

Este archivo explica cómo activar y usar Claude Haiku 4.5 en la aplicación.

Configuración (entorno)

- `ENABLE_CLAUDE_HAIKU`: true/false (o 1/yes). Cuando está en `true`, la aplicación debe usar el modelo indicado.
- `ANTHROPIC_MODEL`: valor por defecto `claude-haiku-4.5`.
- `ANTHROPIC_API_KEY`: tu clave privada de Anthropic. No subirla a repositorios.

Ejemplo rápido de uso en código Django:

```python
from django.conf import settings

if settings.ENABLE_CLAUDE_HAIKU:
    model = settings.ANTHROPIC_MODEL
    # Llamar a tu cliente/servicio de IA con `model`
```

Pasos recomendados para activar para todos los clientes:

1. Añadir las variables al entorno (por ejemplo con `.env` o en tu servidor):
   - `ENABLE_CLAUDE_HAIKU=true`
   - `ANTHROPIC_MODEL=claude-haiku-4.5`
   - `ANTHROPIC_API_KEY=<tu_clave>`
2. (Opcional) Implementar un wrapper cliente en `proservice/ai_client.py` que lea `settings.ANTHROPIC_MODEL` y use la SDK de Anthropic.
3. Actualizar los puntos de integración (views, workers, APIs) para elegir el modelo cuando `ENABLE_CLAUDE_HAIKU` sea verdadero.

Notas:

- No incluyo la llamada concreta a la API de Anthropic aquí porque requiere la SDK y tu clave. Puedo añadir un wrapper de ejemplo si quieres.
