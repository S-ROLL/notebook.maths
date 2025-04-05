# Key tools

## Requirements Files

```
pip install -r requirements.txt
```

- File example:

![alt text](<Screenshot 2024-08-27 at 21.41.30.png>)

## MS SQL Set up

### Stop & Remove Docker

```
docker stop <container_id>
docker rm <container_id>
```

### Set up new port

```
docker run \
  -e "ACCEPT_EULA=Y" \
  -e "MSSQL_SA_PASSWORD=VeryStr0ngP@ssw0rd" \
  --name XXX \
  -p 143X:1433 \
  -v sql_server:/var/opt/mssql \
  --restart=always \
  --hostname sql \
  --platform linux/amd64 \
  -d mcr.microsoft.com/mssql/server:2022-latest
```

| Field       | Value                  |
|-------------|------------------------|
| Server      | `localhost,14333`      |
| User name   | `sa`                   |
| Password    | `YourPassWord@123`   |
| Encrypt     | Mandatory              |
| Trust Cert  | ✅ True                |

### Confirm

```
docker ps
```