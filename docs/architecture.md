# Architecture

User
   |
Azure App Service
   |
Deployment Slots
 ├── Production Slot (Blue)
 └── Staging Slot (Green)

Deployment Strategy:
- Validate staging
- Perform slot swap
- Zero downtime release
