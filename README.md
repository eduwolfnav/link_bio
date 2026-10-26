# link_bio — Mi App de Aprendizaje Fullstack 🐺

> **Objetivo:** Aprender a construir y desplegar una app web real 100% en Python, desde el código en mi PC hasta producción.

Este repo es mi laboratorio. Empezó como un simple Linktree y lo fui convirtiendo en una app fullstack para entender todo el flujo: frontend, backend, APIs, base de datos y deploy automático.

🔗 **Proyecto en vivo:** https://eduwolfnav.vercel.app/
🔗 **Backend (API):** https://eduwolfnav.up.railway.app/

[Demo link_bio](./assets/captura_linkbio.png)

## 🎯 Qué quería aprender

1.  **Reflex:** Crear UI reactiva solo con Python, sin JS
2.  **Componentización:** Separar `components/`, `views/`, `styles/` como en React
3.  **APIs propias:** Crear endpoints con `link_bio/api/api.py`, `SupabaseAPI.py`, `TwitchAPI.py`
4.  **Integración externa:** Conectar Supabase como DB y Twitch API
5.  **Deploy real:** Entender el flujo GitHub -> Vercel (frontend estático) + Railway (backend Docker)
6.  **Automatización:** GitHub Actions que genera el `public/` y hace commit automático
7.  **Problemas reales de prod:** Case-sensitive en Linux, assets que no se copian, `.web` cacheado, merge commits por la Action

## 🛠️ Stack que estoy practicando

| Yo uso esto | Para aprender | Logo |
|---|---|---|
| **Python** | Lógica, tipado, `requirements.txt` | `python.jpg` |
| **Reflex** | Framework fullstack | `reflexlogo.jpg` |
| **FastAPI** (dentro de Reflex) | Routing API | `fastapi.jpg` |
| **Supabase** | DB + env vars | `supabase.jpg` |
| **Docker** | Dockerfile del backend | `dockerfile.jpg` |
| **GitHub Actions** | Static Build `remote_build.yml` | `github.jpg` |
| **Vercel** | Hosting frontend `public/` | `vercel.jpg` |
| **Railway** | Hosting backend API | `railway.jpg` |

## 📁 Estructura que fui armando

```
link_bio/
├── .github/workflows/remote_build.yml  # -> Mi Action de Static Build
├── assets/                             # Todo lo estático que aprendí a servir
│   ├── captura_linkbio.png
│   ├── python.jpg, fastapi.jpg, reflexlogo.jpg...
│   └── python.png, mongodb.png, etc.
├── link_bio/
│   ├── components/          # Aprendí a reutilizar componentes
│   │   ├── link_sponsor.py  # <- donde fallaba reflex.jpg por mayúscula
│   │   └── ...
│   ├── views/               # Vistas: header, sponsors, links
│   │   ├── sponsors.py      # Colaboran - donde mapeo las 8 techs
│   │   └── ...
│   ├── api/                 # Mi primer backend real
│   │   ├── api.py
│   │   ├── SupabaseAPI.py
│   │   └── TwitchAPI.py
│   ├── styles/
│   └── link_bio.py          # Entry point
├── rxconfig.py              # Aprendí CORS y api_url apuntando a Railway
├── Dockerfile               # Receta para Railway
├── requirements.txt
├── local_build.sh           # Build estático en mi PC
├── remote_build.sh          # El que corre en GitHub Actions
├── public/                  # Build generado (no se edita a mano)
├── Flujo_Despliegue_link_bio.svg
└── Cómo se despliega link_bio.pdf
```

Para ver la estructura completa en tu PC, puedes correr:

```powershell
tree /F
# o si tienes git bash
find . -type f -name "*.py" | sort
```

## 🔄 Flujo de despliegue que documenté

Lo tengo en `Cómo se despliega link_bio.pdf`:

1.  `git push origin master` desde VS Code
2.  GitHub avisa en paralelo a 3 servicios: **Static Build**, **Vercel**, **Railway**
3.  Static Build corre en Ubuntu 3.13: `reflex init` + `reflex export --frontend-only`
4.  Hace commit automático `Update static build` con `public/`
5.  Ese commit vuelve a disparar Vercel y Railway
6.  Vercel sirve `public/`, Railway construye desde `Dockerfile`

```
Tu PC -> GitHub -> Vercel (frontend) + Railway (backend)
           |
           +-> Action (Static Build) -> commit public/ -> Vercel
```

> Lección clave: hacer `git pull` siempre antes de `push`, porque la Action te deja 1 commit atrás y te aparece el MERGE_MSG.

## 🚀 Cómo correrlo para aprender

```bash
git clone https://github.com/eduwolfnav/link_bio.git
cd link_bio

python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Crear .env (no se sube a GitHub)
# SUPABASE_URL=...
# SUPABASE_PUBLISHABLE_KEY=...
# TWITCH_CLIENT_ID=...

reflex run
# http://localhost:3000 (frontend)
# http://localhost:8000 (backend)
```

## 📝 Bitácora de aprendizaje

- **Error 1:** `reflex.jpg` no cargaba → era mayúscula `Reflex.jpg` en Linux, en Windows funciona
- **Error 2:** `assets/` no se subía → estaba en `.gitignore` o no estaba trackeado
- **Error 3:** `git status` decía `clean` pero faltaba el archivo → `public/` estaba commiteado y `assets/` no
- **Error 4:** `MERGE_MSG` cada vez que hago pull → es por el commit automático de la Action
- **Solución:** `git rm --cached`, renombrar en 2 pasos, `git add -f`, y `public/` a `.gitignore`

## Próximos pasos de aprendizaje

- [ ] Agregar tests con pytest
- [ ] Agregar página `/cursos` dinámica desde Supabase (ya empezaste `_cursos_._index`)
- [ ] Proteger API con variables en Railway/Vercel
- [ ] Quitar `public/` del repo y dejar solo la Action como fuente de verdad

---
Hecho como app de aprendizaje — By Edu Wolf 🐺 | Oct 2026 | Basado en curso de MoureDev + docs de Reflex
