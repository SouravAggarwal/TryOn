# TryOn – AI-Powered Virtual Clothing Try-On

TryOn is a full-stack web application that lets users virtually try on clothing items using AI technology. Shoppers can upload a photo and see how garments look on them before purchasing, reducing returns and improving the online shopping experience.

> **Live App:** [http://tryon-frontend.s3-website-us-east-1.amazonaws.com/](http://tryon-frontend.s3-website-us-east-1.amazonaws.com/)

---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Frontend Setup](#frontend-setup)
   - [Backend Setup](#backend-setup)
5. [Environment Variables](#environment-variables)
6. [API Reference](#api-reference)
7. [Frontend Routes](#frontend-routes)
8. [Deployment](#deployment)
   - [Frontend – AWS S3 + CloudFront](#frontend--aws-s3--cloudfront)
   - [Backend – AWS EC2](#backend--aws-ec2)
9. [CI/CD Pipeline](#cicd-pipeline)
10. [Contributing](#contributing)

---

## Features

- **Virtual Try-On** – Upload a photo and preview clothing items on yourself before buying.
- **Image Upload API** – RESTful API for uploading and managing try-on images.
- **Responsive Landing Page** – Animated hero section, use-case showcase, affiliate logos, and newsletter sign-up.
- **Pricing Page** – Three subscription tiers: Basic ($9/mo), Pro ($29/mo), and Enterprise (custom).
- **Admin Dashboard** – Django admin panel for managing uploads and users.
- **CI/CD Automation** – GitHub Actions pipelines for automated frontend and backend deployments.

---

## Tech Stack

### Frontend

| Technology | Version | Purpose |
|---|---|---|
| [Vue.js](https://vuejs.org/) | 3.4.38 | UI framework (Composition API + `<script setup>`) |
| [Vue Router](https://router.vuejs.org/) | 4.2.5 | Client-side routing |
| [TypeScript](https://www.typescriptlang.org/) | 5.5.3 | Type-safe JavaScript |
| [Vite](https://vitejs.dev/) | 5.4.2 | Build tool and development server |
| [Tailwind CSS](https://tailwindcss.com/) | 3.4.1 | Utility-first CSS framework |
| [GSAP](https://gsap.com/) | 3.12.5 | Animation library (hero section) |
| [@vueuse/core](https://vueuse.org/) | 10.7.2 | Vue Composition API utilities |
| [@headlessui/vue](https://headlessui.com/) | 1.7.19 | Accessible headless UI components |

### Backend

| Technology | Version | Purpose |
|---|---|---|
| [Django](https://www.djangoproject.com/) | 5.1.5 | Web framework |
| [Django REST Framework](https://www.django-rest-framework.org/) | 3.15.2 | REST API toolkit |
| [django-cors-headers](https://github.com/adamchainz/django-cors-headers) | 4.6.0 | Cross-Origin Resource Sharing (CORS) |
| [django-filter](https://django-filter.readthedocs.io/) | 24.3 | Queryset filtering for API |
| [Pillow](https://pillow.readthedocs.io/) | 11.1.0 | Image processing |
| [Gunicorn](https://gunicorn.org/) | 23.0.0 | WSGI production server |

### Infrastructure

| Service | Purpose |
|---|---|
| AWS S3 | Static frontend hosting |
| AWS CloudFront | CDN for global frontend distribution |
| AWS EC2 (Amazon Linux) | Backend application server |
| Nginx | Reverse proxy for the Django app |
| GitHub Actions | CI/CD automation |

---

## Project Structure

```
TryOn/
├── Frontend/                        # Vue 3 + TypeScript SPA
│   ├── src/
│   │   ├── components/              # Reusable Vue components
│   │   │   ├── NavBar.vue           # Sticky navigation bar
│   │   │   ├── HeroSection.vue      # Animated landing hero
│   │   │   ├── UseCaseSection.vue   # Benefits for individuals & businesses
│   │   │   ├── AffiliateSection.vue # Partner/brand showcase
│   │   │   ├── NewsletterSection.vue# Email subscription form
│   │   │   └── Pricing.vue          # Pricing card component
│   │   ├── views/
│   │   │   ├── Home.vue             # Landing page (assembled sections)
│   │   │   └── Pricing.vue          # Dedicated pricing page
│   │   ├── router/
│   │   │   └── index.ts             # Vue Router configuration
│   │   ├── assets/                  # Static images and icons
│   │   ├── App.vue                  # Root component
│   │   ├── main.ts                  # Application entry point
│   │   └── style.css                # Global styles
│   ├── public/                      # Public static assets
│   ├── package.json
│   ├── vite.config.ts
│   ├── tailwind.config.js
│   ├── tsconfig.json
│   └── postcss.config.js
│
├── Backend/                         # Django REST API
│   ├── tryon_backend/               # Django project configuration
│   │   ├── settings.py              # App settings (DB, CORS, installed apps)
│   │   ├── urls.py                  # Root URL dispatcher
│   │   ├── wsgi.py                  # WSGI entrypoint
│   │   └── asgi.py                  # ASGI entrypoint
│   ├── core/                        # Main Django application
│   │   ├── models.py                # UploadedImage model
│   │   ├── views.py                 # UploadedImageViewSet (CRUD)
│   │   ├── serializers.py           # DRF serializer for UploadedImage
│   │   ├── urls.py                  # API URL routing
│   │   ├── admin.py                 # Django admin registration
│   │   └── migrations/              # Database migration files
│   ├── manage.py
│   └── requirements.txt
│
├── setup/                           # Deployment and infrastructure guides
│   ├── backend_django.md            # Django, EC2, and SSH setup guide
│   ├── deployment_steps.md          # Build and deployment steps
│   ├── aws_cli.md                   # AWS CLI and CloudFront configuration
│   └── GithubWorkflow/              # Notes on GitHub Actions configuration
│
├── .github/
│   └── workflows/
│       ├── frontend_deployment.yml  # Frontend CI/CD (build → S3 → CloudFront)
│       └── backend_core_deployment.yml # Backend CI/CD (SSH → pull → restart)
│
├── LocalFiles/                      # Local development assets
└── .gitignore
```

---

## Getting Started

### Prerequisites

- **Node.js** ≥ 18 and **npm** ≥ 9
- **Python** ≥ 3.11 and **pip**
- **Git**

---

### Frontend Setup

```bash
# Navigate to the frontend directory
cd Frontend

# Install dependencies
npm install

# Start the development server (http://localhost:3000)
npm run dev
```

**Production build:**

```bash
# Build optimized assets into dist/
npm run prod:build

# Install a static file server (first time only)
sudo npm install -g serve

# Serve the production build on http://localhost:3001
npm run prod:serve
```

Available scripts:

| Script | Description |
|---|---|
| `npm run dev` | Start Vite dev server on port 3000 |
| `npm run build` | Type-check with `vue-tsc` then bundle with Vite |
| `npm run prod:build` | Alias for `npm run build` (used in CI) |
| `npm run prod:serve` | Serve the `dist/` folder on port 3001 |
| `npm run preview` | Preview the built app locally via Vite |

---

### Backend Setup

```bash
# Navigate to the backend directory
cd Backend

# Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# (Optional) Create a superuser for the Django admin panel
python manage.py createsuperuser

# Start the development server (http://localhost:8000)
python manage.py runserver 0.0.0.0:8000
```

Access the Django admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/).

---

## Environment Variables

The backend reads standard Django environment settings. For production, set the following:

| Variable | Description | Default |
|---|---|---|
| `SECRET_KEY` | Django secret key | Auto-generated (change in production) |
| `DEBUG` | Enable debug mode | `True` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames | `*` |
| `DATABASE_URL` | Database connection string | SQLite3 at `db.sqlite3` |

**GitHub Actions secrets** (required for CI/CD deployments):

| Secret | Description |
|---|---|
| `AWS_ACCESS_KEY_ID` | AWS IAM access key for S3 uploads |
| `AWS_SECRET_ACCESS_KEY` | AWS IAM secret key for S3 uploads |
| `AWS_REGION` | AWS region (e.g., `us-east-1`) |
| `AWS_S3_BUCKET` | S3 bucket name (e.g., `tryon-frontend`) |
| `CLOUDFRONT_DISTRIBUTION_ID` | CloudFront distribution ID for cache invalidation |
| `EC2_SSH_KEY` | Private SSH key for EC2 deployment |
| `HOST_DNS` | EC2 instance public DNS hostname |
| `EC2_USERNAME` | EC2 SSH username (e.g., `ec2-user`) |

---

## API Reference

Base URL: `http://localhost:8000/api/v1/`

All image endpoints accept and return `application/json`. Image uploads use `multipart/form-data`.

### Uploaded Images

| Method | Endpoint | Description | Request Body |
|---|---|---|---|
| `GET` | `/api/v1/uploads/` | List all uploaded images | – |
| `POST` | `/api/v1/uploads/` | Upload a new image | `image` (file, multipart) |
| `GET` | `/api/v1/uploads/{id}/` | Retrieve a specific image | – |
| `PUT` | `/api/v1/uploads/{id}/` | Replace an image record | `image` (file, multipart) |
| `PATCH` | `/api/v1/uploads/{id}/` | Partially update a record | Any field |
| `DELETE` | `/api/v1/uploads/{id}/` | Delete an image record | – |

**Example – Upload an image:**

```bash
curl -X POST http://localhost:8000/api/v1/uploads/ \
  -F "image=@/path/to/photo.jpg"
```

**Example response:**

```json
{
  "id": 1,
  "image": "/media/uploads/photo.jpg",
  "uploaded_at": "2024-01-15T10:30:00Z"
}
```

---

## Frontend Routes

| Path | Component | Description |
|---|---|---|
| `/` | `Home.vue` | Main landing page |
| `/pricing` | `Pricing.vue` | Subscription plans and pricing |

---

## Deployment

### Frontend – AWS S3 + CloudFront

1. Build the application:
   ```bash
   cd Frontend && npm run prod:build
   ```
2. Sync the `dist/` folder to the S3 bucket:
   ```bash
   aws s3 sync dist/ s3://<your-bucket-name>/ --delete
   ```
3. Invalidate the CloudFront cache:
   ```bash
   aws cloudfront create-invalidation \
     --distribution-id <your-distribution-id> \
     --paths "/*"
   ```

> See [`setup/aws_cli.md`](setup/aws_cli.md) for detailed AWS CLI configuration.

### Backend – AWS EC2

**First-time EC2 setup:**

```bash
# Update packages and install dependencies
sudo yum update && sudo yum upgrade -y
sudo yum install nginx python3.11 -y
sudo yum groupinstall "Development Tools" -y
curl -O https://bootstrap.pypa.io/get-pip.py && python3.11 get-pip.py

# Clone the repository and set up the environment
git clone git@github.com:SouravAggarwal/TryOn.git
cd TryOn/Backend/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

# Start the application server
gunicorn tryon_backend.wsgi --bind 0.0.0.0:8000
```

Configure Nginx as a reverse proxy forwarding port 80 to Gunicorn on port 8000, then start both services:

```bash
sudo systemctl restart nginx
sudo systemctl restart gunicorn
```

> See [`setup/backend_django.md`](setup/backend_django.md) for the complete EC2 setup and SSH key configuration guide.

---

## CI/CD Pipeline

Deployments are fully automated via **GitHub Actions**.

### Frontend Workflow (`.github/workflows/frontend_deployment.yml`)

Triggered on pushes to `main` that modify files under `Frontend/**`.

1. Check out the repository.
2. Install Node.js dependencies (`npm install`).
3. Build the production bundle (`npm run prod:build`).
4. Upload `dist/` to the S3 bucket (`aws s3 sync`).
5. Invalidate the CloudFront distribution cache.

### Backend Workflow (`.github/workflows/backend_core_deployment.yml`)

Triggered on pushes to `main` that modify files under `Backend/**`.

1. SSH into the EC2 instance using the stored private key.
2. Pull the latest code from the `main` branch.
3. Install any new Python dependencies.
4. Restart Gunicorn and Nginx services.

> See [`setup/GithubWorkflow/`](setup/GithubWorkflow/) for additional workflow notes.

---

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request against the `main` branch.

Please follow the existing code style:
- **Frontend:** Vue 3 Composition API with `<script setup>` and TypeScript.
- **Backend:** Django REST Framework conventions with class-based views.
