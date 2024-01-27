const express = require('express');
const { Server } = require("socket.io");
const http = require('http');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

const PORT = process.env.PORT || 4000

app.get('/', (req, res) => {
  res.send('Hii!')
});

io.on('connect', (socket) => {
  console.log('a user connected');
});

io.on("message", async (sid, message)=>{
  await io.emit("message", {input: 'Input', output: "Output", chat_history: 'History'})
})

io.on("disconnect", (sid)=>{
  console.log("Disconnected", sid);
})

server.listen(PORT, () => {
  console.log(`listening on *:${PORT}`);
});