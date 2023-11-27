Launch via 'docker compose up --build' (drop --build flag if no image changes required)

compose.yaml notes:
- Check that 'context' values match the relative path to the respective Dockerfiles
- Check that 'ports' exposes the proper ports for the outward-facing container (i.e. the user-accessible endpoints)
- Check that the hostname of internal containers (e.g. the 'cookie-svc') is used in any requests made to those
    containers
    - Consider using the 'link' key/value to set the hostname that will be used to connect to internal containers
- 'image' key/value can be used to set image name, but isn't really necessary except for setting readable names if
    doing debugging/digging around in the Docker CLI