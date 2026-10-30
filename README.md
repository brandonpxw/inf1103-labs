# INF1103 DevOps Labs

Weekly lab work for **INF1103 – DevOps** at the Singapore Institute of Technology ICT, Software Engineering.

The main project is a command-line **Inventory Management System** written in Python using object-oriented design. Earlier labs, which build up to it, are kept in [`earlier-labs/`](earlier-labs/).

## Running with Docker

Build the image:

```bash
docker build -t inf1103/inventory-system .
```

Run it interactively:

```bash
docker run -it --rm inf1103/inventory-system
```

To keep inventory changes between runs, mount a named volume over the data folder:

```bash
docker run -it --rm -v inventory-data:/app/data inf1103/inventory-system
```
