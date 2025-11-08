# Simwire Flask Application Template

Welcome! I created this repository to make building, testing, and deploying Flask applications for the cloud **accessible for everyone**—especially for junior developers and small teams, but robust enough for seasoned professionals.

As a product owner, my mission is simple:
- **Lower the barrier** for cloud-native backend development.
- **Promote best practices** with built-in testing, CI/CD, and modular code organization.
- **Empower you** to focus on your application’s business logic, _not_ on boilerplate or DevOps plumbing.

## Why Did I Build Simwire?

When I started, I saw that most tools and templates fell into two camps:

- **“Kitchen sink” frameworks** like Django, which are powerful but can be overwhelming and force you into heavyweight structures.
- **UI-focused low-code platforms**, which make interface building easy but ignore backend best practices, DevOps, and proper testing.

**Simwire is my answer:**
- Minimal, scalable, and cloud-friendly.
- Lets you build fast by giving you ready-made structures and cloud deployment patterns.
- Ensures projects start with the right architecture: separation of concerns, automated testing, modularity, and extensible configuration.

## Codebase Structure (What’s Inside)

Here’s a quick breakdown of the project layout to help you get started:

### simwire/
- **/migrations/** – Alembic-powered database migrations for schema changes.
- **/templates/** – Raw HTML, with Jinja templating support.
- **/tests/** – Example and general test cases (like route testing for `/`). Start here with your own tests!
- **/models/** – SQLAlchemy data models (typical example: the `user` table).
- **/dblib/** – Quick, practical API-style routes for ad-hoc DB data access (great for AJAX calls). No need for full OOP structure—just results!
- **/blueprints/**  
  - `home_blueprint`: Single-file example for modular development.
  - `/auth`: Larger packaged blueprint showing modular design in practice—clean separation of views (routes), logic (auth_dao), and initialization (`__init__.py`).

### Top Level Files
- **.env.local** – Local environment vars. _This file is for your dev machine only. Don’t deploy it!_
- **env_load.py** – Manages environment files for easier config management.
- **__init__.py** – Sets up core application & database.
- **app.py** – Central collection point for application wiring.
- **views.py** – Top-level routes (not tied to modules/blueprints).

- **__main__.py** – Webserver entry point (run your app here!).
- **docker-compose.yml** & **Dockerfile** – Everything you need to run locally and mirror your cloud setup (for AWS ECS, etc.).
- **.ebignore** – Ignore files/folders on AWS ElasticBeanstalk deployments.
- **requirements.txt** – Easy dependency management.
- **.github/** – GitHub Actions workflows, CI/CD, and issue/PR templates—ready to use if you fork or template the repository.

## How Do You Use This Repository?

1. **Fork or Use as a Template:** Use the GitHub template feature to start your project.
2. **Configure:** Update `.env.local` for your machine; add environment files as needed for production or test.
3. **Develop:** Add your business logic in `/models`, `/views`, `/blueprints`, and build templates in `/templates`.
4. **Test:** Write or extend tests in `/tests`—testing is first-class here!
5. **Deploy:** Use Docker/Docker Compose locally, and follow the included recipes for cloud setup (ECS, ElasticBeanstalk).

## What Should You Not Modify?

To keep your project up-to-date and compatible with future improvements:
- **Be cautious when modifying core files** like Dockerfile, docker-compose.yml, requirements.txt, env_load.py, and anything in `.github/`. You will often need to customize these files (for example, to add dependencies or adjust Docker settings), but try to preserve their overall structure and review any comments or documentation before making changes. If possible, keep changes minimal and well-documented to make future updates easier.
- Extend the codebase in `/models`, `/views`, `/blueprints`, `/dblib`, and `/tests`.

## The Value for You

Whether you’re a solo developer, teaching juniors, or building a larger team product:
- **Rapid onboarding:** Start with best practices _baked in_.
- **Cloud-ready from Day One:** Local dev mirrors production.
- **Easy updates:** Core features and infrastructure can be improved without breaking your application logic.
- **Professional CI/CD:** Out-of-the-box automation for testing and deployment.

---

_Thank you for considering Simwire. I’d love to hear feedback, and I welcome contributions! Let’s raise the bar for backend apps—together._

---
