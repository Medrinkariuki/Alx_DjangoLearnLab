# Social Media API

A simple Django REST Framework API for a social media app with user authentication.

---

## Features

- Custom User model with:
  - `username`, `email`
  - `bio`
  - `profile_picture`
  - `followers` (many-to-many)
- User Registration (`/api/accounts/register/`)
- User Login (`/api/accounts/login/`) with token authentication

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd social_media_api_project