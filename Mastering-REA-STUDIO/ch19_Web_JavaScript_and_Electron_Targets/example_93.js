const { app, BrowserWindow } = require("electron");
const path = require("node:path");

app.whenReady().then(() => {
  const win = new BrowserWindow({
    width: 480,
    height: 320,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
      contextIsolation: true,
      sandbox: true,
    },
  });
  win.loadFile("index.html");
});
app.on("window-all-closed", () => app.quit());
