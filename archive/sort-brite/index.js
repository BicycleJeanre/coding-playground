const { app, BrowserWindow } = require('electron')

let windowSize = {width: 800, Height: 600}
let mainHTML = "./index.html"
  
 function createWindow(size, HTML){
    let mainWindow = new BrowserWindow(size)
    mainWindow.loadFile(HTML)
    return mainWindow
  }

  async function startWhenAppReady(ws, HTML){
    await app.whenReady()
    return createWindow(ws, HTML)
  }

  let applicationWindow = startWhenAppReady(windowSize, mainHTML)
