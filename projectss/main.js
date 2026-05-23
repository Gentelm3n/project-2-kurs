const { app, BrowserWindow, ipcMain } = require('electron/main')
const path = require('node:path')

let mainWindow

function createWindow () {
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    });
    mainWindow.loadFile('./frontend/main.html')
    mainWindow.webContents.openDevTools()
}

// Функция для загрузки страниц
function loadPage(pageName) {
    const pages = {
        index: 'index.html',
        main: 'main.html'
    };

    mainWindow.loadFile('./frontend/main.html');
}

ipcMain.handle('navigate-to', (event, pageName) => {
    console.log(`Навигация на страницу: ${pageName}`);
    loadPage(pageName);
});

ipcMain.handle('open-new-window', (event, pageName, options = {}) => {
    const { width = 600, height = 400, modal = false } = options;

    const childWindow = new BrowserWindow({
        width,
        height,
        parent: modal ? mainWindow : null,
        modal,
        webPreferences: {
            nodeIntegration: false,
            contextIsolation: true,
            preload: path.join(__dirname, 'preload.js')
        }
    });

    if (isDev) {
        childWindow.loadURL(`http://localhost:3000/${pageName}.html`);
    } else {
        childWindow.loadFile(path.join(__dirname, `../src/pages/${pageName}.html`));
    }

    return childWindow.id;
});


app.whenReady().then(() => {
    createWindow()

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow()
        }
    })
})

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})