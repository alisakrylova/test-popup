# Setup Instructions

1. Install Docker for your system.
2. Clone the repository.
3. Navigate to the repository directory.
4. Run:

    ```bash
    docker compose build --no-cache
    ```

    ```bash
    docker compose up
    ```

    Wait for Docker to execute the commands.
5. View the container's testing logs:
   
   ```bash
   docker logs pytest
   ```