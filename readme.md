Workflow:
1. Let user acess upload page, user uploads image
2. Flask passes the image to the ML app.
3. ML app runs
4. When Ml app is done, flask serves webpage with new image

Considerations:
1. Setup deployment from the get-go
2. Integrate with db (preferable sqlalchemy)
