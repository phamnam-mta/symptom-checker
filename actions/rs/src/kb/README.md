## Neo4j Setup & Cheat Sheet


1. Install Neo4j
    - Mac/Ubuntu: [here](https://debian.neo4j.com/?_gl=1*1eoa08o*_ga*ODgyMDU5OTkxLjE2NDI0NzQ2NzQ.*_ga_DL38Q8KGQC*MTY0NzU3Njg2Ni45LjEuMTY0NzU3ODI2Ny4w&_ga=2.266559563.436929685.1647572439-882059991.1642474674)
    
    This will be a management tools the local/remote severs.  

    - verify installation
    ```bash
    neo4j --version
    neo4j 3.5.14
    ```
    - check sever status
    ```bash
    sudo systemctl status neo4j.service
    ```
    - disable service
    ```bash
    sudo systemctl stop neo4j.service
    ```
    - start service
    ```bash
    sudo systemctl start neo4j.service
    ```

    For the first time, your `user`='neo4j' , `password`='neo4j'. Go to your browser address bar (usually is `http://localhost:7474/`):
    - login
    - change password
2. Export path
```bash
export NEO4J_URL = 'http://localhost:7474/'
export NEO4J_AUTH = '[your_user]/[your_password]'
```
