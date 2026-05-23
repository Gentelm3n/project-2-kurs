const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    navigateTo: (pageName) => {
        return ipcRenderer.invoke('navigate-to', pageName);
    },

    openNewWindow: (pageName, options) => {
        return ipcRenderer.invoke('open-new-window', pageName, options);
    },
});