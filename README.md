# link_bio — Edu Wolf Nav 🐺

Mi página personal de enlaces, hecha 100% en Python con [Reflex](https://reflex.dev/).

🔗 **Demo en producción:** https://eduwolfnav.vercel.app/

[Captura link_bio](./assets/captura_linkbio.png)

### ¿Qué hace?

Es mi Linktree personal:

- **Header** con avatar y presentación
- **Recursos** / **Contacto** / **Cursos**
- **Colaboran** — sponsors con logos (Python, FastAPI, Reflex, Docker, GitHub, Vercel, Railway, Supabase)
- Datos dinámicos desde Supabase y la API de Twitch (`SupabaseAPI.py`, `TwitchAPI.py`)

### Stack

- **Frontend:** Reflex + Python 3.13
- **Backend/API:** Reflex API (Dockerfile)
- **Base de datos:** Supabase
- **Hosting Frontend:** Vercel -> eduwolfnav.vercel.app
- **Hosting Backend:** Railway -> eduwolfnav.up.railway.app
- **Versionado:** GitHub

### Cómo se despliega

Este repo tiene un flujo automático con 3 servicios:

1. Haces `git push origin master`
2. GitHub avisa a: **Static Build (Actions)**, **Vercel** y **Railway**
3. La Action `remote_build.yml` corre `remote_build.sh`: instala deps, hace `reflex init` + `reflex export --frontend-only` y genera `public/` + `frontend.zip`
4. Hace commit automático `Update static build` con la carpeta `public/`
5. Vercel publica el frontend estático y Railway publica el backend desde el Dockerfile

> Diagrama completo: [`Flujo_Despliegue_link_bio.svg`](./Flujo_Despliegue_link_bio.svg) y [`Cómo_se_despliega_link_bio.pdf`](./Cómo_se_despliega_link_bio.pdf)

```
Tu PC --git push--> GitHub --commits--> Vercel (frontend) + Railway (backend)
                        |
                        +--> GitHub Action (Static Build) --commit--> public/ --> Vercel
```

### Estructura clave

```
link_bio/
├── assets/               # Imágenes estáticas (avatar, sponsors, captura)
│   ├── captura_linkbio.png
│   └── ...
├── link_bio/
│   ├── components/       # Componentes UI
│   ├── views/            # sponsors.py, header.py, index_links.py, etc.
│   ├── api/              # api.py, SupabaseAPI.py, TwitchAPI.py
│   └── styles/
├── rxconfig.py           # Config Reflex (api_url a Railway + CORS)
├── Dockerfile            # Build del backend
├── requirements.txt
├── local_build.sh        # Build estático local
├── remote_build.sh       # Build estático en GitHub Actions
└── public/               # Frontend estático generado (lo sirve Vercel)
```

### Correr en local

```bash
# 1. Clonar
git clone https://github.com/eduwolfnav/link_bio.git
cd link_bio

# 2. Entorno
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 3. Variables (.env no se sube a Git)
# Crea un .env con SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, etc.

# 4. Run
reflex run
# Frontend en http://localhost:3000
# Backend en http://localhost:8000
```

### Recomendaciones

- Haz `git pull` antes de cada `push` (la Action crea un commit extra en master)
- Configura `Watch Paths` en Railway para ignorar `public/**` y no reiniciar el backend innecesariamente
- Mantén `.env` fuera de GitHub, cárgalo desde los paneles de Railway y Vercel

---

Built with Reflex — By Edu Wolf 🐺 | 2026
