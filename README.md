# India Economic Data Analysis Dashboard

## Overview

This project provides an interactive dashboard for visualising key Indian economic indicators. It combines a **FastAPI** backend that aggregates data from various public sources (MoSPI, RBI, etc.) and a **React + Vite** frontend with modern UI/UX features:

- **KPI cards** for quick glances at CPI, IIP, GDP, Forex, and more.
- **Dynamic charts** built with `recharts` (line, bar, area charts).
- **Dataset pages** for PLFS, WPI, Energy, and HCES, each with:
  - A **ToggleBar** that shows selected sub‑datasets as removable chips.
  - An **Add** button opening a searchable multi‑select **SubsetsDropdown** modal.
  - **Persistence** of selections via `localStorage` so they survive reloads.
- **Dark‑mode palette, glass‑morphism modal, micro‑animations** for a premium look.
- **Responsive design** for desktop, tablet, and mobile.

## Repository Structure

```
India economic data analysis/
├─ backend/                # FastAPI server
│   ├─ main.py             # API entry point
│   ├─ fetcher.py          # Data fetching & filtering logic
│   └─ test_*.py           # Unit tests for backend
├─ frontend/               # React + Vite UI
│   ├─ src/
│   │   ├─ App.jsx         # Root component with routing
│   │   ├─ App.css
│   │   ├─ index.css
│   │   ├─ components/
│   │   │   ├─ ToggleBar.jsx
│   │   │   └─ SubsetsDropdown.jsx
│   │   └─ pages/
│   │       ├─ PlfsPage.jsx
│   │       ├─ WpiPage.jsx
│   │       ├─ EnergyPage.jsx
│   │       └─ HcesPage.jsx
│   └─ vite.config.js
├─ requirements.txt        # Python dependencies
├─ package.json            # NPM dependencies (react‑router‑dom, recharts…) 
└─ README.md               # *You are reading it now*
```

## Prerequisites

- **Python 3.10+**
- **Node 18+** and **npm**
- Git (optional, for version control)

## Setup

### Backend
```bash
# Navigate to the project root
cd "c:/SHAILESH/My work space/India economic data analysis"

# (Optional) create a virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows PowerShell

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server (auto‑reload on changes)
uvicorn backend.main:app --reload
```
The API will be available at `http://localhost:8000/api/`.

### Frontend
```bash
# In a new terminal, navigate to the frontend folder
cd "c:/SHAILESH/My work space/India economic data analysis/frontend"

# Install NPM packages (including react‑router‑dom)
npm install

# Start the Vite dev server
npm run dev
```
The UI will be served at `http://localhost:5173` (or the port displayed by Vite).

## API Endpoints
| Method | Path | Description |
|--------|------|-------------|
| `GET`  | `/api/data` | Returns a JSON payload with all datasets (cpi, iip, gdp, rbi, plfs, wpi, energy, hces). Supports optional query parameters to filter subsets: `plfs_subset`, `wpi_group`, `energy_type`, `hces_category`.
| `POST` | `/api/refresh` | Forces a fresh scrape of MoSPI/RBI data and returns the updated payload.

## Frontend Routes
| Route | Component | Purpose |
|-------|-----------|---------|
| `/`   | `MainDashboard` | Home view with KPI cards and main charts.
| `/plfs` | `PlfsPage` | PLFS dataset with toggle‑bar & dropdown.
| `/wpi` | `WpiPage` | WPI dataset.
| `/energy` | `EnergyPage` | Energy consumption data.
| `/hces` | `HcesPage` | Household Consumption Expenditure Survey.

## Styling & Aesthetics
- **Colors:** Custom HSL dark‑mode palette (e.g., `--primary: hsl(240, 60%, 55%)`).
- **Glass‑morphism modal:** Backdrop blur with semi‑transparent background for the dropdown.
- **Micro‑animations:** `framer-motion`‑style fade‑in for chips, slide‑down for the modal, smooth line transitions on charts.
- **Responsive layout:** CSS Grid for KPI and chart sections, media queries for mobile breakpoints.

## Testing
```bash
# Backend tests (pytest)
pytest backend

# Frontend component tests (React Testing Library)
npm test
```
The tests cover:
- API filtering logic for each new dataset.
- Rendering of `ToggleBar`, chip removal, and `SubsetsDropdown` modal.
- Persistence of selections via `localStorage`.

## Building for Production
```bash
# Build the frontend bundle
npm run build

# Serve the compiled assets with any static server or integrate into FastAPI:
# (example) fastapi.staticfiles.StaticFiles(directory="frontend/dist")
```
The built bundle can be deployed to any static hosting platform (Netlify, Vercel) or served directly from the FastAPI backend.

## License
This project is licensed under the **MIT License**.

---
**Happy analysing!**
If you need further assistance (e.g., adding new datasets, customizing the UI, or deploying to a cloud environment), just let me know.
