# Example for develops FastAPI in CONTAINER with VSCode

Chinese content please follow here -> [如何在 VSCode 中以 Container 方式開發 FastAPI + PostgreSQL](https://nijialin.com/2021/05/29/fastapi-dev-in-container-vscode/)

## Prerequisite

- VSCode
  - Extension
    - Python
    - Remote Container

## Development

- Open project with VSCode.
- Install `Remote - Containers` VSCode dependency.
- Press `Command` + `Shift` + `p` (Mac).
- Input `Remote Containers: Reopen in Container`.
- Left-side you will find `Run & Debug`, click it and find `►` button.
- Choose `Python: FastAPI` to run this project.
- Then bottom-side would become different color.(Mean you run success)

## Note

- LINE Login JWT [verify document](https://developers.line.biz/zh-hant/docs/line-login/integrate-line-login/#verify-id-token)
- Code example: [LINE Login 實作](https://nijialin.com/2019/10/05/Day21-LINE-Login-%E5%AF%A6%E4%BD%9C/)
- Logger dict needs to be `str()`

### LINE Login Frontend query Backend API steps

> 8080 is default

- GET: http://localhost:8000/login/uri
  - Get LINE login redirect uri
- POST: http://localhost:8000/login
  - Verify and Get login information
  - It will check LINE user info and save to SQL

## License

MIT