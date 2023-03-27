# Sistema Atlas Histologia

## Documentación Básica :)

### Ejecución con Docker y docker-compose

Solo se requiere que los servicios de docker y docker-compose se encuentren activos. Si no están activos se los debe iniciar:

```sh
systemctl start docker
```

Finalmente se ejecuta en la ubicación del archivo `docker-compose.yaml`:
```sh
docker-compose up -d
```
Donde `-d` iniciará el servicio en segundo plano pudiendo así cerrar la sesión ssh.

Para detener el servicio:
```sh
docker-compose down
```

### Replicación del Entorno de Trabajo


Clone the repository:

```sh
git clone https://github.com/Red-Umsalud/SistemaAtlasHistologia
```

Enter to the directory and create a new python environment with virtualenv:

```sh
cd SistemaAtlasHistologia
virtualenv env
```

Activate the new python environment:

```sh
source env/bin/activate
```

Install the python libraries:

```sh
pip install -r requirements.txt
```

### Herramientas utilizadas

En el desarrollo del sistema se utilizó:

- Django
- Bootstrap 4
- HTMX
- Django ORM




