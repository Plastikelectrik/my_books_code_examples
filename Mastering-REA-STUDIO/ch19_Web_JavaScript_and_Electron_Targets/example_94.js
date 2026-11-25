const { contextBridge } = require("electron");

contextBridge.exposeInMainWorld("kettleInfo", {
  version: "1.0.0",
});
