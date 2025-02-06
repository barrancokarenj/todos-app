# todos-app

Prerequisites: 
 - Docker Desktop

## Build FastAPI Local Setup Steps:
```bash

1.  Clone the repository

    $ git clone https://github.com/barrancokarenj/todos-app.git todos-app

2.  Navigate inside todos-app/todo-fastapi folder

    $ cd todos-app/todo-fastapi

3. Copy contents of .env.example to .env and modify as needed, or use the default for local development

4. Execute the following command

   $ docker compose up --build -d

5. Access http://localhost:3001/docs to check if server is running

```

## Build NuxtJS Client Local Setup Steps:

```bash

1. Navigate inside todos-app/todo-client folder

   $ cd todos-app/todo-client

2. Install dependencies

   $ npm i

3. Copy contents of .env.example to .env, and modify as needed, or use the default for local development

4. Start at localhost:3000

   $ npm run dev

5. Access http://localhost:3000

```

