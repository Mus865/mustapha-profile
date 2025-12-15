
# Simple NGINX static site (no docker-compose)
FROM nginx:alpine

# Copy your site files into the default nginx web root
COPY src/html/ /usr/share/nginx/html/

# Optional: health check (container-only)


EXPOSE 80


# Healthcheck against a lightweight /health endpoint
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -qO- http://localhost:8080/health || exit 1
