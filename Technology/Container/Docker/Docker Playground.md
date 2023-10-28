### Working with volumes

```
requirements.txt

pandas
openpyxl
```

```python
import pandas as pd
import sys

def main():
    filepath = sys.argv[1]
    df = pd.read_excel(filepath)
    print(df)

if __name__ == "__main__":
    main()
```

```bash
FROM python:3.9

WORKDIR /app

COPY . .

RUN chmod +x main.py

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "./main.py"]
```

```bash
docker build -t docker-volume .
```

```bash
docker run -v D:\Temp:/data docker-volume /data/example.xlsx
```

```bash
docker run -it -rm -v D:\local:/remote --entrypoint /bin/bash docker-volume
```

1. **ENTRYPOINT**: Defines the executable that will run when the container starts. It's like setting the default application that will handle all commands sent to the container. When you use `docker run <image> <command>`, `<command>` gets appended to the `ENTRYPOINT`.
    
2. **CMD**: Specifies arguments that will be fed into the `ENTRYPOINT`. If `ENTRYPOINT` is not explicitly set, `CMD` will act as the executable, but only if you don't override it with the `docker run <command>` command-line argument.
    
3. **Combination**: When you have both `ENTRYPOINT` and `CMD`, the `CMD` values get passed as default parameters to the `ENTRYPOINT`. These can be overridden by additional command-line arguments when using `docker run`.
    

Here's why `ENTRYPOINT` works for your use case:

- You set `ENTRYPOINT ["python", "./main.py"]`. This makes sure the container always runs `python ./main.py` at startup.
- When you use `docker run -v D:\Temp:/data docker-volume /data/example.xlsx`, the `/data/example.xlsx` argument gets appended to `ENTRYPOINT`, effectively running `python ./main.py /data/example.xlsx`. This is exactly what you want.

<hr>

#docker #container 

